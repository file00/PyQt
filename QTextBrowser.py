# QTextBrowser
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("textbrowserTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_Print.clicked.connect(self.printTextFunction)
        self.btn_setText.clicked.connect(self.changeTextFunction)
        self.btn_appendText.clicked.connect(self.appendTextFunction)
        self.btn_Clear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self) :
        print(self.textbrow_Test.toPlainText())

    def changeTextFunction(self) :
        self.textbrow_Test.setPlainText("This is Textbrowser - Change Text")

    def appendTextFunction(self) :
        self.textbrow_Test.append("Append Text")

    def clearTextFunction(self) :
        self.textbrow_Test.clear()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()