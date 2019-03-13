__author__ = 'Maxim Bykov @ Egor Koemets'
from Controller.Controller import MainController
import sys
from PyQt5.QtWidgets import QApplication

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_controller = MainController()
        self.main_controller.show_window()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())