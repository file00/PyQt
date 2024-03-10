# QTextBrowser
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("ui_File")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Code that assigns a function to the button
        self.btn_Print.clicked.connect(self.printTextFunction)
        self.btn_setText.clicked.connect(self.changeTextFunction)
        self.btn_appendText.clicked.connect(self.appendTextFunction)
        self.btn_Clear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self) :
        # self.Textbrowser'name'.toPlainText()
        # How to get characters in Textbrowser
        print(self.textbrow_Test.toPlainText())

    def changeTextFunction(self) :
        # self.Textbrowser'name'.toPlainText()
        # How to get characters in Textbrowser
        self.textbrow_Test.setPlainText("This is Textbrowser - Change Text")

    def appendTextFunction(self) :
        # self.Textbrowser'name'.append()
        # How to get characters in Textbrowser
        self.textbrow_Test.append("Append Text")

    def clearTextFunction(self) :
        # self.Textbrowser.clear()
        # How to erase letters in Textbrowser
        self.textbrow_Test.clear()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
