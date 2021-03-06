# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(448, 506)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(320, 280))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(360, 340))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 433, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout_4.setContentsMargins(10, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.wavelength_inp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wavelength_inp.sizePolicy().hasHeightForWidth())
        self.wavelength_inp.setSizePolicy(sizePolicy)
        self.wavelength_inp.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.wavelength_inp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.wavelength_inp.setObjectName("wavelength_inp")
        self.gridLayout_4.addWidget(self.wavelength_inp, 13, 1, 1, 1)
        self.fileinp_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.fileinp_text.setText("")
        self.fileinp_text.setObjectName("fileinp_text")
        self.gridLayout_4.addWidget(self.fileinp_text, 0, 0, 1, 2)
        self.logtext = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.logtext.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logtext.sizePolicy().hasHeightForWidth())
        self.logtext.setSizePolicy(sizePolicy)
        self.logtext.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logtext.setObjectName("logtext")
        self.gridLayout_4.addWidget(self.logtext, 22, 1, 1, 1)
        self.int_cutoff = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.int_cutoff.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.int_cutoff.setObjectName("int_cutoff")
        self.gridLayout_4.addWidget(self.int_cutoff, 19, 1, 1, 1)
        self.loadcif_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loadcif_btn.setObjectName("loadcif_btn")
        self.gridLayout_4.addWidget(self.loadcif_btn, 17, 1, 1, 1)
        self.tolerance_inp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.tolerance_inp.setObjectName("tolerance_inp")
        self.gridLayout_4.addWidget(self.tolerance_inp, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 19, 0, 1, 1)
        self.opn_folder_btn = QtWidgets.QToolButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opn_folder_btn.sizePolicy().hasHeightForWidth())
        self.opn_folder_btn.setSizePolicy(sizePolicy)
        self.opn_folder_btn.setObjectName("opn_folder_btn")
        self.gridLayout_4.addWidget(self.opn_folder_btn, 0, 2, 1, 1)
        self.do_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.do_btn.setObjectName("do_btn")
        self.gridLayout_4.addWidget(self.do_btn, 22, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 13, 0, 1, 1)
        self.dspacings_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dspacings_line.sizePolicy().hasHeightForWidth())
        self.dspacings_line.setSizePolicy(sizePolicy)
        self.dspacings_line.setMaximumSize(QtCore.QSize(340, 16777215))
        self.dspacings_line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.dspacings_line.setText("")
        self.dspacings_line.setObjectName("dspacings_line")
        self.gridLayout_4.addWidget(self.dspacings_line, 10, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setToolTip("")
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 5, 0, 1, 1)
        self.dspacings_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dspacings_btn.sizePolicy().hasHeightForWidth())
        self.dspacings_btn.setSizePolicy(sizePolicy)
        self.dspacings_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.dspacings_btn.setText("")
        self.dspacings_btn.setObjectName("dspacings_btn")
        self.gridLayout_4.addWidget(self.dspacings_btn, 10, 2, 1, 1)
        self.clean_diamonds_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.clean_diamonds_cb.setEnabled(True)
        self.clean_diamonds_cb.setChecked(True)
        self.clean_diamonds_cb.setObjectName("clean_diamonds_cb")
        self.gridLayout_4.addWidget(self.clean_diamonds_cb, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 18, 0, 1, 1)
        self.d_min_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_min_input.sizePolicy().hasHeightForWidth())
        self.d_min_input.setSizePolicy(sizePolicy)
        self.d_min_input.setMaximumSize(QtCore.QSize(10000, 16777215))
        self.d_min_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.d_min_input.setObjectName("d_min_input")
        self.gridLayout_4.addWidget(self.d_min_input, 18, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 10, 0, 1, 1)
        self.opn_mask_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.opn_mask_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.opn_mask_btn.setObjectName("opn_mask_btn")
        self.gridLayout_4.addWidget(self.opn_mask_btn, 7, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 6, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_4.addWidget(self.line_9, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 14, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_4.addWidget(self.line_6, 20, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deltatheta_inp = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deltatheta_inp.sizePolicy().hasHeightForWidth())
        self.deltatheta_inp.setSizePolicy(sizePolicy)
        self.deltatheta_inp.setMinimumSize(QtCore.QSize(25, 0))
        self.deltatheta_inp.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.deltatheta_inp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.deltatheta_inp.setObjectName("deltatheta_inp")
        self.horizontalLayout.addWidget(self.deltatheta_inp)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.deltatheta_linear = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.deltatheta_linear.setObjectName("deltatheta_linear")
        self.horizontalLayout.addWidget(self.deltatheta_linear)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.deltatheta_square = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.deltatheta_square.setObjectName("deltatheta_square")
        self.horizontalLayout.addWidget(self.deltatheta_square)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.gridLayout_4.addLayout(self.horizontalLayout, 11, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_4.addWidget(self.line_5, 20, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_4.addWidget(self.line_10, 1, 1, 1, 1)
        self.mask_lineedit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.mask_lineedit.setObjectName("mask_lineedit")
        self.gridLayout_4.addWidget(self.mask_lineedit, 7, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 11, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 6, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_4.addWidget(self.line_7, 9, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_4.addWidget(self.line_8, 9, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 14, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 8, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.p02mask_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.p02mask_cb.setObjectName("p02mask_cb")
        self.horizontalLayout_2.addWidget(self.p02mask_cb)
        self.id15mask_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.id15mask_cb.setObjectName("id15mask_cb")
        self.horizontalLayout_2.addWidget(self.id15mask_cb)
        self.iddmask_cb = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.iddmask_cb.setObjectName("iddmask_cb")
        self.horizontalLayout_2.addWidget(self.iddmask_cb)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 8, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PeakСleaner 0.4 M.Bykov E. Koemets 2019"))
        self.wavelength_inp.setText(_translate("MainWindow", "0.2900"))
        self.fileinp_text.setPlaceholderText(_translate("MainWindow", "provide .tabbin file"))
        self.logtext.setText(_translate("MainWindow", "<html><head/><body><p>Please provide .tabbin file (<span style=\" color:#ff0000;\">wd t</span>)</p></body></html>"))
        self.int_cutoff.setText(_translate("MainWindow", "10"))
        self.loadcif_btn.setText(_translate("MainWindow", "Generate d-spacings from cif"))
        self.tolerance_inp.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Intensity cutoff for cif"))
        self.opn_folder_btn.setText(_translate("MainWindow", "..."))
        self.do_btn.setText(_translate("MainWindow", "Clean Peaks"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Wavelength</p></body></html>"))
        self.dspacings_line.setPlaceholderText(_translate("MainWindow", "separated by space"))
        self.label.setText(_translate("MainWindow", "Tolerance (pixels)"))
        self.clean_diamonds_cb.setText(_translate("MainWindow", "Clean Diamonds?"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Minimum d-spacing for cif</p></body></html>"))
        self.d_min_input.setText(_translate("MainWindow", "0.9"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Clean <span style=\" font-style:italic;\">d</span>-spacings</p></body></html>"))
        self.opn_mask_btn.setText(_translate("MainWindow", "..."))
        self.deltatheta_inp.setText(_translate("MainWindow", "0.2"))
        self.deltatheta_inp.setPlaceholderText(_translate("MainWindow", "Δd"))
        self.label_6.setText(_translate("MainWindow", "+"))
        self.deltatheta_linear.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "θ"))
        self.label_8.setText(_translate("MainWindow", "+"))
        self.deltatheta_square.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p> θ<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Times New Roman,serif\'; font-size:9pt;\">Δ2θ  =</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Dioptas mask file "))
        self.label_12.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">P02</span> - Perkin Elmer Detector</p><p><br/><span style=\" font-weight:600;\">ID15</span> - Mar555 detector. </p><p>Works if CrysAlis files are in <span style=\" font-weight:600;\">.esperanto</span> format and Dioptas mask was created based on <span style=\" font-weight:600;\">.mar2560</span> file. Tested with Dioptas 0.5.0. <span style=\" color:#ff0000;\">Might be not pixel precise. Try to grow mask a bit</span></p><p><br/><span style=\" font-weight:600;\">13 IDD</span> - works for CrysAlis experiments created after June 2019</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">?</span></p></body></html>"))
        self.p02mask_cb.setText(_translate("MainWindow", "P02"))
        self.id15mask_cb.setText(_translate("MainWindow", "ID15"))
        self.iddmask_cb.setText(_translate("MainWindow", "13 IDD"))


