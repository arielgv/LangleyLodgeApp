#!/usr/bin/env python
# coding: utf-8

# # WORKING PROGRAM
# This program takes the old.csv and compares it with the main.csv. It creates the file "eliminados.csv," which shows the names that need to be deleted from Shopify, and also creates "nuevos.csv," which displays the names that need to be added to Shopify. This is gonna be performed by the program in the next steps.
# # Instructions : 
# This next cell is gonna download both files needed from the datasource (Sheet 1, general books, and Sheet 2 Non-fiction and cooking). and auto-renamed to be compatible with the script.

# In[5]:


import requests
def download_google_sheet_as_csv(sheet_id, sheet_gid=0, output_filename='default.csv'):
    """
    THIS SCRIPT DOWNLOADS BOTH CSV FILES AND SAVES AS 'MAIN.CSV' AND 'MAIN2.CSV'

    """
    
    GOOGLE_SHEET_CSV_URL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={sheet_gid}"
    
    try:
        response = requests.get(GOOGLE_SHEET_CSV_URL)
        response.raise_for_status()  
        
        with open(output_filename, 'wb') as file:
            file.write(response.content)
        
        return True
        
    except requests.RequestException as e:
        print(f"Error al descargar el archivo: {e}")
        return False


SHEET_ID_MAIN = "1IT0gCm4h_pYmKRQIGjpctvUrxP-3TY_Mk9fg0ONpXc4" 
SHEET_ID_NONFICTION = "1fsefcNPi4EU7fugQBcosdN_QpuSl3cZgVaufrOzVPw4"
download_google_sheet_as_csv(SHEET_ID_MAIN, 0, output_filename="main.csv")
download_google_sheet_as_csv(SHEET_ID_NONFICTION,0,output_filename="main2.csv")


# In[6]:


import csv

def process_line(line):

    in_quotes = False
    new_line = ''
    for ch in line:
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == ',' and not in_quotes:
            new_line += ';'
            continue
        new_line += ch
    return new_line.replace('"', '') # Remover comillas al final

def append_file_content(src_filename, dest_filename, start_line=0):
    with open(src_filename,'r') as src_file, open(dest_filename, 'a') as dest_file:
        lines = src_file.readlines()[start_line:]
        for line in lines:
            if "cookbooks start" in line.lower():
                continue
            dest_file.write(line)

append_file_content('main2.csv', 'main.csv', start_line=5)

with open('main.csv', 'r') as input_file, open('new.csv', 'w') as output_file:
    for line in input_file:
        output_file.write(process_line(line))


def clean_row(row):
    return row.replace(';', '').strip()

def read_and_clean_csv(filename):
    with open(filename, 'r') as f:
        return [clean_row(row) for row in f.readlines()[6:]]

def write_to_file(filename, data):
    with open(filename, 'w', newline='') as f:
        for row in data:
            f.write(row + '\n')

def compare_and_write(old_csv, new_csv):
    old_data = set(read_and_clean_csv(old_csv))
    new_data = set(read_and_clean_csv(new_csv))

    removed = old_data - new_data
    added = new_data - old_data

    write_to_file('eliminados.csv', removed)
    write_to_file('nuevos.csv', added)

compare_and_write('old.csv', 'new.csv')


# # STARTING TO POST ON SHOPIFY
# Run this cell and its going to start posting the books

# In[10]:


import shopify
import os


shop_url = "https://f6d2681f67f7cc5d6a2d6e3a014895fd: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@lodgeauxiliary.myshopify.com/admin"
shopify.ShopifyResource.set_site(shop_url)

counter = 0

nombre_del_archivo_csv = 'nuevos.csv'
with open(nombre_del_archivo_csv, 'r', encoding='utf-8-sig') as f:
    for line in f:
        try:
            formatted_title = line.strip().replace(' ', '%20').replace(',', '')
            image_url = f"https://raw.githubusercontent.com/arielgv/booksource3/main/IMG_3314.jpg"
            print("url = ", image_url)

            file_name = line.strip()
            print("file_name and title = ", file_name)

            first_letter = file_name[0].upper()
            if first_letter.isalpha():
                tag = first_letter
            else:
                tag = ""  # Si no es alfabética, no se asigna tag

            new_product = shopify.Product()
            new_product.title = file_name 
            new_product.product_type = "Print Books"
            new_product.vendor = "lodgeauxiliary"
            new_product.tags = tag
            variant = shopify.Variant({
                'price': '1.00', 
                'compare_at_price': '1.00',
                'inventory_management': 'shopify'
            })
            new_product.variants = [variant]

            new_image = shopify.Image()
            new_image.src = image_url
            new_product.images = [new_image]

            new_product.save()

            if new_product.errors:
                print(new_product.errors)
            else:
                print("Product created successfully., ID: ", new_product.id)
                counter += 1
                print('counter : ', counter)

                location_id = 62699864200  # Location ID real
                inventory_item_id = new_product.variants[0].inventory_item_id

                inventory_adjustment = shopify.InventoryLevel.adjust(location_id, inventory_item_id, 1)
                if inventory_adjustment.errors:
                    print(inventory_adjustment.errors)
                else:
                    print("Inventory adjusted successfully.")
        except Exception as e:
            print(f"Error processing the line. {line.strip()}: {e}")


# # Delete the sold items.
# Take the file "eliminados.csv" and delete what is found in it.
# 
# Run this cell:

# In[ ]:


import shopify
import os

shop_url = "https://3d961aa8665da23e801a75bd2d7bb0b7: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@lodgeauxiliary.myshopify.com/admin"
shopify.ShopifyResource.set_site(shop_url)

nombre_del_archivo_csv = 'eliminados.csv'
with open(nombre_del_archivo_csv, 'r', encoding='utf-8-sig') as f:
    for line in f:
        try:
            product_title = line.strip()
            print("Product title to delete = ", product_title)

            products = shopify.Product.find(title=product_title)

            if not products:
                print(f"Product {product_title} not found.")
                continue

            for product in products:
                product.destroy()
                if product.errors:
                    print(product.errors)
                else:
                    print(f"Product {product_title} Successfully deleted., ID: {product.id}")

        except Exception as e:
            print(f"Error processing the line.{line.strip()}: {e}")


# The files used will be saved as archived in the "USED" folder with their datetime. The file "main.csv" that was used will be renamed to "old.csv". The images will be moved to "USED/images".
# Run this cell:

# In[ ]:


import os
import datetime

old_file = 'old.csv'
eliminados_file = 'eliminados.csv'
nuevos_file = 'nuevos.csv'
new_file = 'new.csv'
used_folder = 'USED'
main_file = 'main.csv'

date = datetime.datetime.now().strftime("%d_%m_%Y")

def rename_and_move(filename, new_name):
    os.rename(filename, new_name)
    os.replace(new_name, os.path.join(used_folder, new_name))

if os.path.exists(old_file):
    rename_and_move(old_file, f'old{date}.csv')

if os.path.exists(eliminados_file):
    rename_and_move(eliminados_file, f'eliminados{date}.csv')

if os.path.exists(nuevos_file):
    rename_and_move(nuevos_file, f'nuevos{date}.csv')

if os.path.exists(new_file):
    os.rename(new_file, old_file)

if os.path.exists(main_file):
    rename_and_move(main_file, f'main{date}.csv')

try: 
    images_folder = 'images'
    image_files = os.listdir(images_folder)

    for image_file in image_files:
        full_image_path = os.path.join(images_folder, image_file)
        if os.path.isfile(full_image_path):
            os.replace(full_image_path, os.path.join(used_folder, images_folder, image_file))
except:
    print('')


# In[ ]:




