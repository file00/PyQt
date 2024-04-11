# Basic Image Output
from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([])
label = QtWidgets.QLabel()
pixmap = QtGui.QPixmap('Image_File (with Path)')
label.setPixmap(pixmap)
label.resize(pixmap.width(),pixmap.height())
label.show()

app.exec_()
