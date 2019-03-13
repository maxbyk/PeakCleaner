from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from qtpy import QtGui
from Widgets.Mainwidget import Ui_MainWindow

class MainWidget(QMainWindow):
    def __init__(self):
        QtGui.QWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)