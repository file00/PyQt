# QComboBox
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui_File")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.syncComboBox()

        self.cmb_Test.currentIndexChanged.connect(self.comboBoxFunction)

        self.btn_printItem.clicked.connect(self.printComboBoxItem)
        self.btn_clearItem.clicked.connect(self.clearComboBoxItem)
        self.btn_addItem.clicked.connect(self.addComboBoxItem)
        self.btn_deleteItem.clicked.connect(self.deleteComboBoxItem)

    def syncComboBox(self) :
        for i in range(0,self.cmb_Test.count()) :
            self.cmb_second.addItem(self.cmb_Test.itemText(i))

    def comboBoxFunction(self) :
        self.lbl_display.setText(self.cmb_Test.currentText())

    def clearComboBoxItem(self) :
        self.cmb_Test.clear()
        self.cmb_second.clear()

    def printComboBoxItem(self) :
        print(self.cmb_second.currentText())

    def addComboBoxItem(self) :
        self.cmb_Test.addItem(self.lineedit_addItem.text())
        self.cmb_second.addItem(self.lineedit_addItem.text())
        print("Item Added")

    def deleteComboBoxItem(self) :
        self.delidx = self.cmb_second.currentIndex()
        self.cmb_Test.removeItem(self.delidx)
        self.cmb_second.removeItem(self.delidx)
        print("Item Deleted")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 