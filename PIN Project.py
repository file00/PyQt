from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import sys
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.lbl = QLabel("Please enter your PIN number", self)
        self.lbl.setAlignment(Qt.AlignCenter)
        self.lbl.move(120, 40)

        self.msgLabel = QLabel("", self)
        self.msgLabel.setAlignment(Qt.AlignCenter)
        self.msgLabel.setGeometry(130, 120, 300, 80)

        # Create 'input' screen
        self.qle = QLineEdit(self)
        self.qle.move(120, 100)
        self.qle.returnPressed.connect(self.onChanged)
        print(self)

        # Default screen settings
        self.setWindowTitle('Widget')
        self.move(500, 500)
        self.resize(400, 200)
        self.show()

    def onChanged(self):
        myText = "----"  # <---- Setting PIN number(You can type what you want)
        input = self.qle.text()

        if myText == input:
            time.sleep(0.1)
            self.onClose()
        else:
            self.msgLabel.setText('Wrong, Try agein!!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
