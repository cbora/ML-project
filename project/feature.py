import numpy as np
from sklearn.preprocessing import normalize

class Feature():

    def __init__(self, file_name='dataset/features.csv'):
        self.file_name = file_name
        self.data  = None
        self.open()
        
    def open(self):
        self.data = np.loadtxt(self.file_name, delimiter=',')

    def get_data(self):
        return self.data

    def get(self, row, col):
        if self.data:
            return self.data[col, row]
        
    def get_col(self, col):
        return self.data[:, col]

    def get_digit(self, index):
        return self.data[index]

    def get_centered(self):
        return (self.data - np.mean(self.data, axis=0))

    def get_normal(self):
        """ Centers and normize data."""
        d = self.data - np.mean(self.data, axis=0)
        d = normalize(self.data, axis=0, norm='l1')
        return d
