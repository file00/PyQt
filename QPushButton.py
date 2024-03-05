# QPushButton
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('ui_File')[0] 

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Code to link a function to a button
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
    def button1Function(self): # Function to work when btn_1 is pressed
        print("btn_1 Clicked")

    def button2Function(self): # Function to work when btn_2 is pressed
        print("btn_2 Clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_() 