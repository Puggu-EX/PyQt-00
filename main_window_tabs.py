# Only needed for access to command line arguments
import sys

from PyQt5.QtWidgets import *

from layout_colorwidget import Color


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')

        rgb = {
            0: "Red",
            1: "Green",
            2: "Blue"
        }

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for i, color in enumerate(["red", "green", "blue"]):
            tabs.addTab(Color(color), color)

        tabs.tabBarClicked.connect(lambda x: self.tab_clicked(x, dict=rgb))
        tabs.currentChanged.connect(lambda x: self.tab_switched(x, dict=rgb))

        self.setCentralWidget(tabs)

    def tab_clicked(self, x, dict):
        print("Tab Clicked!")

    def tab_switched(self, x, dict):
        print("Tab Switched to Color: ", dict[x])
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()
# window.setMinimumSize(590, 360)

app.exec_()
