import tkinter
import os
import csv
from tkinter import *
from tkinter import messagebox


def barcodeQuery():
    # creates list of directories
    directories = os.listdir("Test_Directory")
    # opens csv
    with open("Test_Sample_Data.csv") as f:
        # initializes barcodes as a set
        barcodes = set()
        # skips first 8 rows
        for i, line in enumerate(f):
            if i < 7:
                continue
            # reads csv file
            readCSV = csv.reader(f, delimiter=",")
            for row in readCSV:
                # initializes barcode as element in column 4
                barcode = row[3]
                if barcode not in directories:
                    # adds element in column 4 to set if not in directory
                    barcodes.add(barcode)

        # converts set into string for message box output
        stringBarcodes = "\n".join(barcodes)

    root = Tk()

    tkinter.messagebox.showinfo(
        "Missing Directories",
        "The following directories are missing:\n" + stringBarcodes)
    root.destroy()

barcodeQuery()
