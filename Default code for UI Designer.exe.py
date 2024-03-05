# # Default code for UI Designer.exe
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('MyStudy.ui')[0] # ui file connection (but the ui file must be located in the same directory as the Python code file)

# Class declaration used to display the screen
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        """
        ---------------------------------------------
        Enter the signal
        ---------------------------------------------
        """

if __name__ == "__main__":
    app = QApplication(sys.argv) # QApplication: Class that runs the program.
    myWindow = WindowClass() # Creating an Instance of Window Class
    myWindow.show() # Code that shows the program screen
    app.exec_() # Code to enter the program into EventLoop