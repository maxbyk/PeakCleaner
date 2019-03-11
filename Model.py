from PyQt5 import QtCore
import numpy as np
import math
import logging
from struct import *

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.NOTSET)

class PyCleanerModel(QtCore.QObject):

    def __init__(self):
        super(PyCleanerModel, self).__init__()
        self.counter = 0

        self.bad_peaks = []
        self.bad_d_peaks = []

    def create_bad_thetas(self):
        self.bad_thetas = []

        for bad_d in self.dspacings:
            self.bad_thetas.append(2*self.d_to_theta(bad_d))

    def clean_dspacings(self, filename, number_of_peaks):

        f = open(filename, 'r+b')

        self.create_bad_thetas()

        for i in range(number_of_peaks):
            position = 312 + i * 168  # reflection start position

            f.seek(position + 24)  # 2theta position
            theta_byte = f.read(8)
            theta = unpack('d', theta_byte)

            for bad_theta in self.bad_thetas:
                if theta[0] > bad_theta - self.deltatheta and theta[0] < bad_theta + self.deltatheta:
                    f.seek(1118 + number_of_peaks * 168 + i * 32)
                    f.write(b'\x04\x00')
        f.close()

    def theta_to_d(self,theta):
        d = self.wavelength/(2*math.sin(theta))
        return d

    def d_to_theta(self,d):
        theta = math.asin(self.wavelength/(2*d))
        return theta

    def analyze_xy(self, filename, number_of_peaks):

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

        bad_peaks = []

        for i in range(peaks_unique.shape[0]):
            if counters[i] > 2:
                bad_peaks.append([peaks_unique[i][0], peaks_unique[i][1]])

        f.close()

        return bad_peaks

    def delete_peaks(self, filename, bad_peaks, number_of_peaks):

        f = open(filename, 'r+b')

        for i in range(number_of_peaks):
            position = 312 + i * 168  # reflection start position

            f.seek(position + 24)  # 2theta position
            theta_byte = f.read(8)
            theta = unpack('d', theta_byte)

            f.seek(position + 32)  # intensity
            intensity_byte = f.read(4)

            f.seek(position + 44)  # x - coordinate
            x_byte = f.read(2)

            f.seek(position + 46)  # y - coordinate
            y_byte = f.read(2)

            f.seek(1118 + number_of_peaks * 168 + i * 32)

            intensity = int.from_bytes(intensity_byte, byteorder='little')
            x = int.from_bytes(x_byte, byteorder='little')
            y = int.from_bytes(y_byte, byteorder='little')

            comb = [x, y]

            if comb in bad_peaks:
                f.write(b'\x03\x00')

            # out.append([x,y,intensity,theta[0]])
        f.close()

    def read_header(self, filename):
        f = open(filename, 'r+b')
        f.seek(0)
        number_of_peaks = f.read(4)
        number = int.from_bytes(number_of_peaks, byteorder='little')
        return number
