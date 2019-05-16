from PyQt5 import QtCore
import numpy as np
import math
from struct import *
from PyQt5.QtWidgets import QApplication
import fabio
from matplotlib import pyplot

class PyCleanerModel(QtCore.QObject):

    def __init__(self):
        super(PyCleanerModel, self).__init__()

    def clean_peaks_from_mask(self, filename, number_of_peaks, mask_filename):

        f = open(filename, 'r+b')
        try:
            mask = fabio.open(mask_filename)
            #pyplot.imshow(mask.data)
            #pyplot.show()
        except:
            return

        for i in range(number_of_peaks):

            position = 312 + i * 168  # reflection start position

            f.seek(position + 44)  # x - coordinate
            x_byte = f.read(2)

            f.seek(position + 46)  # y - coordinate
            y_byte = f.read(2)

            x = int.from_bytes(x_byte, byteorder='little')
            y = int.from_bytes(y_byte, byteorder='little')

            if mask.data[x,y] == 1:
                f.seek(1118 + number_of_peaks * 168 + i * 32)
                f.write(b'\x04\x00')

        f.close()


    def clean_dspacings(self, filename, number_of_peaks):
        '''Moves peaks with bad d-spacings to the group 5'''

        f = open(filename, 'r+b')

        self.bad_thetas = self.create_bad_thetas(self.dspacings)

        for i in range(number_of_peaks):

            position = 312 + i * 168  # reflection start position

            f.seek(position + 24)  # lambda/d
            ld_byte = f.read(8)
            ld = unpack('d', ld_byte)

            twotheta = 2*math.asin(ld[0]/2)

            for bad_theta in self.bad_thetas:
                delta = self.dtheta[0] + self.dtheta[1]*bad_theta + self.dtheta[2]*bad_theta*bad_theta
                if bad_theta - delta < twotheta < bad_theta + delta:
                    f.seek(1118 + number_of_peaks * 168 + i * 32)
                    f.write(b'\x04\x00')

            QApplication.processEvents()

        f.close()

    def create_bad_thetas(self, dspacings):
        '''Creates a list of 2theta values from a list of d-values'''

        bad_thetas = []

        for bad_d in dspacings:
            bad_thetas.append(2*self.d_to_theta(bad_d))

        return bad_thetas

    def theta_to_d(self, theta):
        '''transforms theta given in radians to d-spacing'''
        d = self.wavelength/(2*math.sin(theta))
        return d

    def d_to_theta(self,d):
        '''transforms d in angstoms to theta in radians'''
        theta = math.asin(self.wavelength/(2*d))
        return theta

    def analyze_xy(self, filename, number_of_peaks, tolerance=2):

        '''returns a set of [x,y] detector coordinates that are common between "tolerance" number of peaks'''

        f = open(filename,'r+b')

        peaks = []

        for i in range(number_of_peaks):
            position = 312 + i * 168  # reflection start position

            f.seek(position + 44)  # x - coordinate
            x_byte = f.read(2)

            f.seek(position + 46)  # y - coordinate
            y_byte = f.read(2)

            x = int.from_bytes(x_byte, byteorder='little')
            y = int.from_bytes(y_byte, byteorder='little')

            peaks.append([x, y])

        peaks.sort()

        peaks_array = np.array(peaks)

        peaks_unique, counters = np.unique(peaks_array, return_counts=True, axis=0)

        bad_peaks = set()

        for i in range(peaks_unique.shape[0]):
            if counters[i] > tolerance:
                bad_peaks.add((peaks_unique[i][0], peaks_unique[i][1]))

        f.close()

        return bad_peaks

    def delete_peaks(self, filename, bad_peaks, number_of_peaks, tolerance=3):
        '''Move all peaks in a file that are present in "bad peaks" to group 4
            Move all peaks within "tolerance" number of pixels around the bad peak to group 3'''

        f = open(filename, 'r+b')

        for i in range(number_of_peaks):
            position = 312 + i * 168  # reflection start position

            f.seek(position + 44)  # x - coordinate
            x_byte = f.read(2)

            f.seek(position + 46)  # y - coordinate
            y_byte = f.read(2)

            f.seek(1118 + number_of_peaks * 168 + i * 32)

            x = int.from_bytes(x_byte, byteorder='little')
            y = int.from_bytes(y_byte, byteorder='little')

            comb = (x, y)

            bad_coordinates = set()

            for i in range(2*tolerance+1):
                for j in range(2*tolerance+1):
                    bad_coordinates.add((x-tolerance+i,y-tolerance+j))

            if comb in bad_peaks:
                f.write(b'\x03\x00')

            elif any(i in bad_coordinates for i in bad_peaks):
                f.write(b'\x03\x00')

            QApplication.processEvents()

        f.close()

    def read_header(self, filename):
        '''reads thte first bytes in the .tab file and returns the total number of peaks'''
        f = open(filename, 'r+b')
        f.seek(0)
        number_of_peaks = f.read(4)
        number = int.from_bytes(number_of_peaks, byteorder='little')
        return number