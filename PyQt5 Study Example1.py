# PyQt5 Study Example1
import sys
import cv2
import numpy as np
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore

form_class = uic.loadUiType('ImageStudy.ui')[0]

class MyMain(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('My Study')
        self.btn_load.clicked.connect(self.file_load)
        self.btn_convert.clicked.connect(self.image_proc)
        self.thresh_parameter_set()
        self.combo_cases = ['Gray Scale', 'Threshold', 'Reverse']
        for case in self.combo_cases:
            self.combo_func.addItem(case)

    def thresh_parameter_set(self):
        self.slider_thr_val.valueChanged.connect(self.slider_set_thr_value)
        self.thr_val = 127
        self.slider_thr_max.valueChanged.connect(self.slider_set_max_value)
        self.thr_max = 255

        self.combo_thr_type.addItem('BINARY', cv2.THRESH_BINARY)
        self.combo_thr_type.addItem('BINARY_INV', cv2.THRESH_BINARY_INV)
        self.combo_thr_type.addItem('TRUNC', cv2.THRESH_TRUNC)
        self.combo_thr_type.addItem('TOZERO', cv2.THRESH_TOZERO)
        self.combo_thr_type.addItem('TOZERO_INV', cv2.THRESH_TOZERO_INV)
        self.combo_thr_type.addItem('BINARY + OTSU', cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        self.combo_thr_type.addItem('BINARY_INV + OTSU', cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        self.combo_thr_type.currentIndexChanged.connect(self.combo_thr_type_changed)

    def combo_thr_type_changed(self):
        self.proc_threshold()

    def slider_set_thr_value(self, value):
        self.lbl_thr_val.setText(f'Thr : ({value:03d})')
        self.thr_val = value
        self.proc_threshold()

    def slider_set_max_value(self, value):
        self.lbl_thr_max.setText(f'Max : ({value:03d})')
        self.thr_max = value
        self.proc_threshold()

    def file_load(self):
        target_path = ''
        fname = QFileDialog.getOpenFileName(self, 'Select File', target_path,
                                            'All File(*);; JPEG File(*.jpg);; PNG File(*.png)')
        if fname[0]:
            self.line_name.setText(fname[0])
            self.image_load(fname[0])
        else:
            self.line_name.setText('None File.')

    def image_proc(self):
        if self.combo_func.currentIndex() == 0:
            self.proc_gray_scale()
        elif self.combo_func.currentIndex() == 1:
            self.proc_threshold()

    def proc_gray_scale(self):
        img_gray = cv2.cvtColor(self.img_src, cv2.COLOR_BGR2GRAY)
        self.display_output_image(img_gray, 'DST')

    def proc_threshold(self):
        img_gray = cv2.cvtColor(self.img_src, cv2.COLOR_BGR2GRAY)
        index = self.combo_thr_type.currentIndex()
        _, img_bin = cv2.threshold(img_gray,
                                   self.thr_val,
                                   self.thr_max,
                                   self.combo_thr_type.itemData(index))
        self.display_output_image(img_bin, 'DST')

    def image_load(self, file_path):
        img_array = np.fromfile(file_path, np.uint8)
        self.img_src = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        self.display_output_image(self.img_src)

    def display_output_image(self, cv_img, mode='SRC'):
        label = self.lbl_img_src if mode == 'SRC' else self.lbl_img_dst
        h, w = cv_img.shape[:2]
        if cv_img.ndim == 2:
            qImg = QImage(cv_img, w, h, w * 1, QImage.Format_GrayScale8)
        else:
            bytes_per_line = cv_img.shape[2] * w
            qImg = QImage(cv_img, w, h, bytes_per_line, QImage.Format_BGR888)
        pixmap = QtGui.QPixmap(qImg)
        p = pixmap.scaled(self.lbl_img_src.width(),
                          self.lbl_img_src.height(),
                          QtCore.Qt.KeepAspectRatio)
        label.setPixmap(p)
        label.update()

    def image_convert(self):
        pass

    def btn_load_clicked(self):
        pass

    def btn_convert_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMain()
    sys.exit(app.exec_())