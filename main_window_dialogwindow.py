# Only needed for access to command line arguments
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


# from layout_colorwidget import Color


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        pagelayout = QVBoxLayout()

        button2 = QPushButton("Press for message box!!")
        button2.clicked.connect(self.button2_clicked)

        pagelayout.addWidget(button2)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def button2_clicked(self, s):
        print("Click Message Box")
        messagebox = QMessageBox()
        messagebox.setWindowTitle("Question Box")
        messagebox.setText("Wuddaya Gay?")
        messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Help)
        messagebox.setIcon(QMessageBox.Question)
        # messagebox.exec_()
        test = messagebox.exec_()

        if test == QMessageBox.Yes:
            print("Like the Cool Kids B)")
        elif test == QMessageBox.No:
            print('2 bad homo, u gey')
        elif test == QMessageBox.Help:
            print('Nope, you gey')
        else:
            print("Failed :<")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
# window.setMinimumSize(590, 360)

app.exec_()
