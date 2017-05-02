
import os
import csv
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


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

        def window():
            app = QApplication(sys.argv)
            # w = QWidget() do I need this??

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(
                "Directory is missing scanned chip information files.      ")
            msg.setWindowTitle("Missing Information")
            msg.setDetailedText(
                "The missing files are as follows:\n" + stringBarcodes)
            msg.setStandardButtons(QMessageBox.Ok)

            msg.show()
            sys.exit(app.exec_())

        if barcodes is not None:
            window()


barcodeQuery()
