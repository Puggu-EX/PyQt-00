# Only needed for access to command line arguments
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()

        self.label = QLabel(self)
        self.label.setText("Testing")
        self.label.setAlignment(Qt.AlignRight)

        self.setCentralWidget(self.label)


# You need only one QApplication instance per application
# Pass in sys.argv to allow command line arguments for you app.
# If you know you won't use command line arguments QApplication([]) work too.
app = QApplication(sys.argv)

window = MainWindow()
# Windows are hidden by default
window.show()
# window.setFixedSize(960, 560)

# Start the event loop
# The purpose of the underscore after *exec* is because exec without the underscore is reserved
# by python
app.exec_()
