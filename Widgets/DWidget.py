from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from qtpy import QtGui
from Widgets.DspacingsWidget import Ui_DSpacings
from PyQt5 import QtGui

class DspacingsWidget(QWidget):
    def __init__(self, data):
        QtGui.QWindow.__init__(self)
        self.ui = Ui_DSpacings()
        self.ui.setupUi(self)
        self.data = data
        self.current_row = 0

        self.set_initial_data(self.data)
        self.ui.dTable.setHorizontalHeaderLabels(['d'])
        self.connect_buttons()

    def set_initial_data(self,data):
        self.ui.dTable.setRowCount(len(data))

        for i, item in enumerate(data):
            newitem = QTableWidgetItem(str(item))
            self.ui.dTable.setItem(0,i,newitem)

    def connect_buttons(self):
        self.ui.table_add_btn.clicked.connect(self.add_btn_clicked)
        self.ui.table_delete_btn.clicked.connect(self.delete_btn_clicked)
        self.ui.dTable.cellClicked.connect(self.get_current_raw)
        self.ui.table_done_btn.clicked.connect(self.done_btn_clicked)

    def add_btn_clicked(self):
        rowPosition = self.ui.dTable.rowCount()
        self.ui.dTable.insertRow(rowPosition)

    def get_current_raw(self, row, column):
        self.current_row = row

    def delete_btn_clicked(self):
        self.ui.dTable.removeRow(self.current_row)

    def done_btn_clicked(self):
        return



