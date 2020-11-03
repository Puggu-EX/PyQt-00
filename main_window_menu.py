# Only needed for access to command line arguments
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


# rom layout_colorwidget import Color


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        widget = QLabel("Hi, I'm a label!")
        widget.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(widget)

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))

        toolbar.setStatusTip("Move Toolbar")

        save_action = QAction(QIcon("assets/icons/disk-black.png"), "Save", self)
        save_action.setStatusTip("Save")
        save_action.triggered.connect(lambda x: self.toolbarClicked(x, "Save"))
        toolbar.addAction(save_action)
        toolbar.addSeparator()

        action = toolbar.addAction("1")
        action.setCheckable(True)
        action.triggered.connect(lambda x: self.toolbarClicked(x, 1))
        action.setStatusTip("Dis is numba juan")

        action = toolbar.addAction("2")
        action.triggered.connect(lambda x: self.toolbarClicked(x, 2))
        action.setStatusTip("Dis is numba twoo")
        toolbar.addSeparator()

        action = toolbar.addAction("3")
        action.triggered.connect(lambda x: self.toolbarClicked(x, 3))
        action.setStatusTip("Dis is numba twee")

        action = toolbar.addAction("4")
        action.triggered.connect(lambda x: self.toolbarClicked(x, 4))
        action.setStatusTip("Dis is numba fohr")
        toolbar.addSeparator()

        slider = QSlider()
        slider.setFixedSize(200, 25)
        slider.setTickPosition(QSlider.TickPosition(2))
        slider.setOrientation(Qt.Horizontal)
        slider.setRange(-5, 5)
        slider.setStatusTip("Sliiider")
        slider.valueChanged.connect(lambda x: self.sliderValue(x))
        toolbar.addWidget(slider)
        toolbar.addSeparator()

        # pos = slider.sliderPosition()
        # toolbar.addWidget(QLabel(str(pos)))

        self.addToolBar(toolbar)

        menubar = self.menuBar()

        file_menu = menubar.addMenu("&File")
        file_menu.addAction(save_action)
        save_action.setShortcut("Ctrl+S")

        edit_menu = menubar.addMenu("Edit")
        edit_action = edit_menu.addAction("Testing")

        self.setStatusBar(QStatusBar(self))

    def toolbarClicked(self, x, n):
        print("Click:", n)

    def sliderValue(self, x):
        print(x)


app = QApplication(sys.argv)

window = MainWindow()
window.show()
# window.setMinimumSize(590, 360)

app.exec_()
