"""
Workspace Properties
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class WorkspacePropertiesWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Properties")

        window_layout = QHBoxLayout()
        self.setLayout(window_layout)

        # Tab Properties
        checkbox_group = QGroupBox("Tabs")
        window_layout.addWidget(checkbox_group)

        tab_layout = QVBoxLayout()
        checkbox_group.setLayout(tab_layout)

        tab_main = QCheckBox("Main Tab")
        tab_main.setCheckState(Qt.Checked)
        # tab_main.clicked.connect(lambda x: tab_main.removeTab(x))
        tab_main.clicked.connect(lambda x: self.tabVisibilityProperty(x, 0))
        tab_layout.addWidget(tab_main, alignment=Qt.AlignLeft)

        tab_forces_b = QCheckBox("Forces (Basic)")
        tab_forces_b.setCheckState(Qt.Checked)
        tab_forces_b.clicked.connect(lambda x: self.tabVisibilityProperty(x, 1))
        tab_layout.addWidget(tab_forces_b, alignment=Qt.AlignLeft)

        tab_forces_a = QCheckBox("Forces (Advanced)")
        tab_forces_a.setCheckState(Qt.Checked)
        tab_forces_a.clicked.connect(lambda x: self.tabVisibilityProperty(x, 2))
        tab_layout.addWidget(tab_forces_a, alignment=Qt.AlignLeft)

        tab_incline = QCheckBox("Incline")
        tab_incline.setCheckState(Qt.Checked)
        tab_incline.clicked.connect(lambda x: self.tabVisibilityProperty(x, 3))
        tab_layout.addWidget(tab_incline, alignment=Qt.AlignLeft)

    def tabVisibilityProperty(self, s, index):
        if s is True:
            print("add")
        else:
            print("remove")
