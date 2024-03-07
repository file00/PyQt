# QLabel
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('ui_File')[0] 

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_changeText.clicked.connect(self.changeTextFunction)
        self.btn_printText.clicked.connect(self.printTextFunction)

    def changeTextFunction(self) :
        # self.Label name.setText("String")
        # How to change letters in Label
        self.lbl_Test.setText("This is Label - Change Text")

    def printTextFunction(self) :
        # self.Label name.text()
        # How to get letters in Label
        print(self.lbl_Test.text())

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 
