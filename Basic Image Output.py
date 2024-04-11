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

# Connect cv2 version
# import cv2
# from PyQt5 import QtWidgets
# from PyQt5 import QtGui

# app = QtWidgets.QApplication([])
# label = QtWidgets.QLabel()

# img = cv2.imread('Image_File (with Path)')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# h,w,c = img.shape
# qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)

# pixmap = QtGui.QPixmap.fromImage(qImg)
# label.setPixmap(pixmap)
# label.resize(pixmap.width(),pixmap.height())
# label.show()

# app.exec_()
