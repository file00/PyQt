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
        exitAction = QAction(QIcon('exit.png'),'Exit',self)
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
        btn.move(400,260) # Quit 버튼 위치 이동
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('Python.png'))
        self.setGeometry(300,300,500,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyFirstApplication()
    sys.exit(app.exec_())