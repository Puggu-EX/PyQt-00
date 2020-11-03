# Only needed for access to command line arguments
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


# from layout_colorwidget import Color


# Subclass QMainWindow to customise your application's main window
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('idk')

        pagelayout = QVBoxLayout()

        label = QLabel("Another Window")
        label.setAlignment(Qt.AlignCenter)
        pagelayout.addWidget(label)
        self.setLayout(pagelayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle('My Application')
        button = QPushButton("Push for Window")
        button.clicked.connect(self.show_new_window)
        self.setCentralWidget(button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None


app = QApplication(sys.argv)

window = MainWindow()
window.show()
# window.setMinimumSize(590, 360)

app.exec_()
