
import os
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
            if i < 8:
                continue
            barcode = line.split(",")
            if barcode[3] not in directories:
                barcodes.add(barcode[3])

        # converts set into string for message box output & file output
        stringBarcodes = "\n".join(sorted(barcodes))
        with open("Missing Data.csv", "w") as f:
            f.write(stringBarcodes)

        # creates QMessageBox
        def window():
            app = QApplication(sys.argv)
            # w = QWidget() do I need this??

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(
                "Directory is missing scanned chip information files.    ")
            msg.setWindowTitle("Missing Information")
            msg.setDetailedText(
                "The missing files are as follows:\n" + stringBarcodes)
            msg.setStandardButtons(QMessageBox.Ok)

            msg.show()
            sys.exit(app.exec_())

        # opens QMessageBox if set "barcodes" is populated
        if barcodes:
            window()


barcodeQuery()
