# Only needed for access to command line arguments
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5 import QtWidgets, QtCore, QtGui

from window_properties_win import WindowPropertiesWin
from workspace_properties_win import WorkspacePropertiesWin


class CustomMenu(QMenu):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.addAction('test')


# Preference Windows
class PreferencesWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Preferences")


class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()

        lay = QHBoxLayout()
        self.setLayout(lay)

        self.setStyleSheet('background-color: beige;')
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(175, 20)

        self.setMouseTracking(True)
        self.label.setStyleSheet('border-style: outset;'
                                 'border-width: 2px;'
                                 'border-color: black;')

        # lay.addWidget(self.label)
        # self.setLayout(lay)

    def mouseMoveEvent(self, event):
        self.label.setText('Mouse coords: (x: %d | y: %d )' % (event.x()-605, -event.y()+308))


# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Application')
        self.setFixedSize(1280, 720)

        self.window_properties = WindowPropertiesWin()
        self.workspace_properties = WorkspacePropertiesWin()

        windowlayout = QHBoxLayout()

        self.tab_main = QWidget()
        self.tab_main.layout = QVBoxLayout()
        self.tab_main.setLayout(self.tab_main.layout)

        self.graphicsView = QGraphicsView()
        self.graphicsView.setGeometry(QRect(10, 40, 601, 411))
        scene = QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QPen(Qt.red)
        side = 20
        for i in range(10):
            for j in range(5):
                r = QRectF(QPointF(i * side, j * side), QSizeF(side, side))
                scene.addRect(r, pen)

        self.test = MouseTracker()
        self.tab_main.layout.addWidget(self.test)

        self.tab_forces_b = QWidget()
        self.tab_forces_b.layout = QVBoxLayout()
        self.tab_forces_b.layout.addWidget(QLabel('Forces (Basic)'), alignment=Qt.AlignCenter)
        self.tab_forces_b.layout.addWidget(self.graphicsView)
        self.tab_forces_b.setLayout(self.tab_forces_b.layout)

        self.tab_forces_a = QWidget()
        self.tab_forces_a.layout = QVBoxLayout()
        self.tab_forces_a.layout.addWidget(QLabel('Forces (Advanced)'), alignment=Qt.AlignCenter)
        self.tab_forces_a.setLayout(self.tab_forces_a.layout)

        self.tab = QTabWidget()
        self.tab.setMovable(True)

        self.tab.addTab(self.tab_main, 'Main')
        self.tab.addTab(self.tab_forces_b, 'Forces (Basic)')
        self.tab.addTab(self.tab_forces_a, 'Forces (Advanced)')
        self.tab.tabBarClicked.connect(lambda x: self.tab_clicked(x))

        windowlayout.addWidget(self.tab)

        widget = QWidget()
        widget.setLayout(windowlayout)
        self.setCentralWidget(widget)

        # Tool Bar
        self.toolbar = QToolBar()
        icon_size = QSize(16, 16)
        self.toolbar.setIconSize(icon_size)
        # self.toolbar.setOrientation(Qt.Horizontal)
        # self.toolbar.addWidget(QLabel("Tabs"))
        # self.toolbar.addWidget(QCheckBox("Main"))
        # pixmap = QPixmap("assets/icons/target--plus.png")
        add_point = QAction(QIcon("assets/icons/target--plus.png"), "Add Point", self)
        rem_point = QAction(QIcon("assets/icons/target--minus.png"), "Remove Point", self)
        add_vector = QAction(QIcon("assets/icons/vector--plus.png"), "Add Vector", self)
        rem_vector = QAction(QIcon("assets/icons/vector--minus.png"), "Remove Vector", self)

        self.toolbar.addAction(add_point)
        self.toolbar.addAction(rem_point)
        self.toolbar.addAction(add_vector)
        self.toolbar.addAction(rem_vector)

        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        # Menu Bar
        self.menubar = QMenuBar()
        file_menu = self.menubar.addMenu("File")
        file_menu.addAction("Open File")
        file_menu.addMenu("Open Recent Files")
        file_menu.addAction("Close File")
        file_menu.addSeparator()
        file_menu.addAction("Save")
        file_menu.addAction("Save As...")
        file_menu.addSeparator()
        file_menu.addAction("Preferences")

        edit_menu = self.menubar.addMenu("Edit")
        edit_menu.addAction("Nothing")
        edit_menu.addAction("Noting")

        view_menu = self.menubar.addMenu("View")
        view_menu.addMenu("Workspaces")
        windowprop = view_menu.addAction("Workspace Properties")
        windowprop.triggered.connect(self.openWorkspaceProp)

        self.setMenuBar(self.menubar)

        # Status Bar
        self.setStatusBar(QStatusBar())

        self.setMouseTracking(True)

    def openWindowProp(self):
        # window_properties_win
        self.window_properties.show()

    def openWorkspaceProp(self):
        # workspace_properties_win
        self.workspace_properties.show()

    def closeMyTab(self, index):
        print("Tab Close Request")
        print(index)
        self.tabs.removeTab(index)

    def tab_clicked(self, x):
        print(x)


app = QApplication(sys.argv)
# ex = MouseTracker()

window = MainWindow()
# window.setWindowFlag(Qt.FramelessWindowHint)
window.show()
# window.setMinimumSize(590, 360)
app.exec_()
