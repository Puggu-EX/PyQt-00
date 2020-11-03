from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys


class CustomButton(QButtonGroup):

    def keyPressEvent(self, e):
        super(CustomButton, self).keyPressEvent(e)

    def event(self, e):
        print(e)
        e.accept()


app = QApplication(sys.argv)

window = QMainWindow(flags=QtCore.Qt.WindowStaysOnTopHint)
window.setFixedSize(960, 590)
window.setWindowTitle("Signals, SLots, Events")
window.show()

menubar = QMenuBar()
menu = menubar.addMenu("File")
menu.addAction("test")
menu.addAction("under test")

window.setMenuBar(menubar)

app.exec_()
