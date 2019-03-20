from Widgets.View import MainWidget
from Model.Model import PyCleanerModel
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import Qt
import os
import pyperclip
from Model.CifPhase import CifConverter
import numpy as np
from Widgets.DWidget import DspacingsWidget
from shutil import copyfile

class MainController(object):

    def __init__(self):
        self.widget = MainWidget()
        self.model = PyCleanerModel()
        self.check_dspacings()
        self.check_wavelength()
        self.check_deltatheta()
        self.check_dmin()
        self.check_tolerance()
        self.dialog = DspacingsWidget(self.dspacings)
        self.create_signals()

    def show_window(self):
        self.widget.show()

    def create_signals(self):
        self.widget.ui.opn_folder_btn.clicked.connect(self.open_folder_btn_clicked)
        self.widget.ui.do_btn.clicked.connect(self.clean_peaks)
        self.widget.ui.fileinp_text.textChanged.connect(self.check_filename)
        self.widget.ui.wavelength_inp.textChanged.connect(self.check_wavelength)
        self.widget.ui.dspacings_line.editingFinished.connect(self.check_dspacings)
        self.widget.ui.deltatheta_inp.editingFinished.connect(self.check_deltatheta)
        self.widget.ui.deltatheta_inp.editingFinished.connect(self.check_deltatheta)
        self.widget.ui.d_min_input.editingFinished.connect(self.check_dmin)
        self.widget.ui.loadcif_btn.clicked.connect(self.check_cif)
        self.widget.ui.dspacings_btn.clicked.connect(self.dspacings_btn_clicked)
        self.dialog.ui.table_done_btn.clicked.connect(self.get_dspacings_from_dialog)
        self.widget.ui.tolerance_inp.editingFinished.connect(self.check_tolerance)

    def dspacings_btn_clicked(self):
        self.check_dspacings()
        self.dialog.set_initial_data(self.dspacings)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.show()

    def get_dspacings_from_dialog(self):

        self.dspacings = []
        for i in range(self.dialog.ui.dTable.rowCount()):
            item = self.dialog.ui.dTable.item(i,0)
            if item != None:
                try:
                    self.dspacings.append(float(item.text()))
                except:
                    pass

            self.model.dspacings = self.dspacings

        text = ''
        for dspacing in self.dspacings:
            text += str(round(float(dspacing),3))+' '

        self.widget.ui.dspacings_line.setText(text)
        self.dialog.close()

    def open_folder_btn_clicked(self):
        filename = QFileDialog.getOpenFileName(filter = 'tabbin(*.tabbin)')
        self.widget.ui.fileinp_text.setText(filename[0])
        self.check_filename()

    def clean_peaks(self):
        self.check_filename()
        self.check_dspacings()
        self.check_wavelength()
        self.check_deltatheta()
        self.check_dmin()

        filename, filextension = os.path.splitext(self.filename)
        workfile = filename + '_fixed.tabbin'
        copyfile(self.filename, workfile)
        QApplication.processEvents()

        if self.error_checker():
            QApplication.processEvents()
            self.update_label('Working...','orange')
            QApplication.processEvents()

            self.ref_number = self.model.read_header(workfile)

            self.model.clean_dspacings(workfile, self.ref_number)

            if self.widget.ui.clean_diamonds_cb.isChecked():
                self.bad_peaks = self.model.analyze_xy(workfile, self.ref_number)
                self.model.delete_peaks(workfile, self.bad_peaks, self.ref_number, self.tolerance)

            pyperclip.copy('rd t "' + workfile[:-7]+'"')
            self.update_label('Finished', 'green')

        else:
            return

    def check_filename(self):

        self.filename = self.widget.ui.fileinp_text.text()

        filename, filextension = os.path.splitext(self.filename)

        if filextension == '.tabbin' and os.path.isfile(self.filename):
            self.update_label('Press Start', 'green')
            return True

        elif not os.path.isfile(self.filename):

            self.update_label('File not found','red')
            return False

        elif filextension != '.tabbin':
            self.update_label('Wrong file extension','red')
            return False

    def check_wavelength(self):
        try:
            self.model.wavelength = float(self.widget.ui.wavelength_inp.text())
            self.wavelength = self.model.wavelength
            self.check_filename()
            return True
        except:
            self.update_label('Wrong wavelength','red')
            return False

    def check_dmin(self):
        try:
            self.model.dmin = float(self.widget.ui.d_min_input.text())
            self.dmin = self.model.dmin
            self.check_filename()
            return True
        except:
            self.update_label('Wrong d min', 'red')
            return False

    def check_dspacings(self):
        try:
            dspacings_str = self.widget.ui.dspacings_line.text()

            if dspacings_str == '':
                self.model.dspacings = []
                self.dspacings = self.model.dspacings
                self.check_filename()
                return True
            else:
                dspacings_list = dspacings_str.split()
                self.model.dspacings = [float(d) for d in dspacings_list]
                self.dspacings = self.model.dspacings
                self.check_filename()  
                return True
        except:
            self.update_label('Wrong d-spacings','red')
            return False

    def check_deltatheta(self):
        try:
            self.model.deltatheta = float(self.widget.ui.deltatheta_inp.text())*3.14/180
            self.check_filename()
            return True
        except:
            self.update_label('Wrong delta theta','red')
            return False

    def update_label(self, text, color):
        self.widget.ui.logtext.setText(text)
        self.widget.ui.logtext.setStyleSheet('color:'+color)

    def error_checker(self):
        if self.check_filename() and self.check_dspacings() and self.check_wavelength() and self.check_deltatheta() and self.check_dmin():
            self.update_label('Press Start', 'green')
            return True
        elif not self.check_wavelength():
            self.update_label('Wrong wavelength','red')
            return False
        elif not self.check_dspacings():
            self.update_label('Wrong d-spacings','red')
            return False
        elif not self.check_dmin():
            self.update_label('Wrong d min', 'red')
            return False
        elif not self.check_deltatheta():
            self.update_label('Wrong delta theta','red')
            return False
        elif not self.check_tolerance():
            self.update_label('Wrong tolerance', 'red')
        else:
            self.check_filename()
            return False

    def check_tolerance(self):
        try:
            self.tolerance = int(self.widget.ui.tolerance_inp.text())
            self.check_filename()
            return True
        except:
            self.update_label('Wrong tolerance', 'red')
            return False

    def check_cif(self):

        cif_filename = QFileDialog.getOpenFileName()

        int_cutoff = float(self.widget.ui.int_cutoff.text())
        cif_converter = CifConverter(self.wavelength, self.dmin, int_cutoff)

        try:
            jcpds_object = cif_converter.convert_cif_to_jcpds(cif_filename[0])
        except:
            return

        jcpds_object.compute_d0()
        reflections = jcpds_object.get_reflections()
        res = np.zeros((len(reflections),5))
        for i, reflection in enumerate(reflections):
            res[i, 0] = reflection.d
            res[i, 1] = reflection.intensity
            res[i, 2] = reflection.h
            res[i, 3] = reflection.k
            res[i, 4] = reflection.l

        line = ''
        for i in range(res.shape[0]):
            d = str(round(res[i][0],3))
            line += d + ' '

        self.widget.ui.dspacings_line.setText(line)