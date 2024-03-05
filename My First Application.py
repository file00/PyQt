# - What is PyQt?
# PyQt is a framework that allows you to create GUI programs by connecting Python's code to Qt's layout. 
# PyQt started by creating a tool that converts Qt, C++'s Cross Platform GUI Framework, from Riverbank Computing in the UK to Python modules. Currently, versions of PyQt4 and PyQt5 are mainly used.

# - Characteristics of PyQt
# In Python, there are various GUI frameworks such as PyGTK, PySide, and Tkinter. However, these GUI frameworks are difficult to use and have the disadvantage of not being visually pretty.
# Unlike these frameworks, PyQt has the advantage of being able to design programs easily using a program called Qt Designer while showing a good visual design

import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow, QAction, QWidget, QPushButton, QToolTip, qApp)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication, QDate, Qt

class MyFirstApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('Any photo file is fine.'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        filemenu = menubar.addMenu('&Edit')
        filemenu = menubar.addMenu('&View')
        filemenu = menubar.addMenu('&Help')


        QToolTip.setFont((QFont('SansSerif',10)))
        self.setToolTip('This is a <b>QPushButton</b> widget')
        btn = QPushButton('Quit',self)
        btn.move(400,260) # Move the Quit button position
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('Any photo file is fine.'))
        self.setGeometry(300,300,500,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyFirstApplication()
    sys.exit(app.exec_())
