# QRadioButton
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('ui_File')[0] 

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect the Radio Butons in the GroupBox.
        self.groupBox_rad1.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad2.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad3.clicked.connect(self.groupboxRadFunction)
        self.groupBox_rad4.clicked.connect(self.groupboxRadFunction)
    
        def groupboxRadFunction(self):
        app = QApplication(sys.argv)
        myWindow = WindowClass()
        myWindow.show()
        app.exec_()
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_() 