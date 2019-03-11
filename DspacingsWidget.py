# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dspacingswidget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DSpacings(object):
    def setupUi(self, DSpacings):
        DSpacings.setObjectName("DSpacings")
        DSpacings.resize(241, 315)
        self.dTable = QtWidgets.QTableWidget(DSpacings)
        self.dTable.setGeometry(QtCore.QRect(0, 0, 121, 311))
        self.dTable.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhPreferNumbers)
        self.dTable.setAlternatingRowColors(False)
        self.dTable.setRowCount(1)
        self.dTable.setColumnCount(1)
        self.dTable.setObjectName("dTable")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.dTable.setItem(0, 0, item)
        self.dTable.verticalHeader().setVisible(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(DSpacings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 0, 101, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.table_add_btn.setObjectName("table_add_btn")
        self.verticalLayout.addWidget(self.table_add_btn)
        self.table_delete_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.table_delete_btn.setObjectName("table_delete_btn")
        self.verticalLayout.addWidget(self.table_delete_btn)
        self.table_done_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.table_done_btn.setObjectName("table_done_btn")
        self.verticalLayout.addWidget(self.table_done_btn)

        self.retranslateUi(DSpacings)
        QtCore.QMetaObject.connectSlotsByName(DSpacings)

    def retranslateUi(self, DSpacings):
        _translate = QtCore.QCoreApplication.translate
        DSpacings.setWindowTitle(_translate("DSpacings", "DSpacings"))
        __sortingEnabled = self.dTable.isSortingEnabled()
        self.dTable.setSortingEnabled(False)
        self.dTable.setSortingEnabled(__sortingEnabled)
        self.table_add_btn.setText(_translate("DSpacings", "Add"))
        self.table_delete_btn.setText(_translate("DSpacings", "Delete"))
        self.table_done_btn.setText(_translate("DSpacings", "Apply"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DSpacings = QtWidgets.QWidget()
    ui = Ui_DSpacings()
    ui.setupUi(DSpacings)
    DSpacings.show()
    sys.exit(app.exec_())
