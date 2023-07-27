# Repository Guide

Welcome to LangleyLodge repository! This README will guide you through the necessary steps to successfully download, setup, and run the program. Please, follow each step carefully.

## Table of Contents

1. [Repository Download](#Repository-Download)
2. [Software Installation](#Software-Installation)
    * [Python3](#Python3)
    * [Visual Studio Code](#Visual-Studio-Code)
    * [Shopify Dependency](#Shopify-Dependency)
3. [Project Setup](#Project-Setup)
4. [Program Operation](#Program-Operation)
5. [Maintenance](#Maintenance)

## Repository Download

The first step is to download the content of this repository:

1. Click on the green `Code` button at the top of this page.
2. In the dropdown, click on `Download ZIP`.
3. Save the file to your preferred location in your local system and extract the ZIP file.

## Software Installation

This project requires Python3, Visual Studio Code, and the Shopify dependency. Each is installed as follows:

### Python3

You need Python3 installed on your machine:

1. Visit the official Python website at [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the Python3 installer compatible with your operating system.
3. Run the installer and follow the on-screen instructions to install Python3.

### Visual Studio Code

To visualize and interact with the code, you need Visual Studio Code:

1. Visit the official Visual Studio Code website at [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Download the installer compatible with your operating system.
3. Run the installer and follow the on-screen instructions to install Visual Studio Code.

### Shopify Dependency

The project also requires the Shopify dependency, which can be installed via pip, Python's package installer:

1. Open a terminal/command prompt window.
2. Run the following command: `pip install ShopifyAPI`

_**Note:** These installations, including the Shopify dependency, only need to be done once._

## Project Setup

After downloading and extracting the repository, follow these steps to prepare your project:

1. Navigate to the following URL: [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1IT0gCm4h_pYmKRQIGjpctvUrxP-3TY_Mk9fg0ONpXc4/edit#gid=0)
2. Click on `File` > `Download` > `Comma Separated Values(.csv)`.
3. Rename this CSV file as "main.csv".
4. Move "main.csv" into the same folder where you extracted the repository files(Same folder as the Synchro.ipynb).


## Program Operation

To run the program, follow these steps:

1. Open the Visual Studio Code application.
2. Click `File` > `Open Folder` and select the folder where you extracted the repository files.
3. Open the `Synchro v2.ipynb`  file.
4. Follow the instructions in the script comments to successfully run the program.
   * If a pop-up from Visual Studio Code suggests installing an add-on, click on Install and wait for it to install automatically.

You can execute each code cell by positioning yourself on the rectangle that contains the block of code. A "play" arrow will appear just to the left of it, click on each block to execute them.

On its first run, it may ask if you want to install the Jupyter + Python add-on. Accept and install the suggested extension.

If another pop-up appears the first time it is run, also click on Install. These pop-ups are characteristic of the first run on a computer.

At this point, the program should execute as expected and perform its tasks automatically.

## Maintenance

For future uses of the program, you only need to download the updated spreadsheet from the provided Google Docs link, save it as "new.csv" in the repository folder, and run the program. There's no need to re-install Python, Visual Studio Code, or the Shopify dependency.

We hope this guide helps you to successfully run our program. If you encounter any issues or need further assistance, please, don't hesitate to raise an issue in this repository.
