from PyQt5.QtWidgets import *


# Window Properties
class WindowPropertiesWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Properties")

        windowlayout = QVBoxLayout()

        cbox_always_on_top = QCheckBox()
        cbox_always_on_top.checkState()

        windowlayout.addWidget(cbox_always_on_top)

        self.setLayout(windowlayout)
