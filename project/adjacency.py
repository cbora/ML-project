import numpy as np

class Adjacency():

    def __init__(self, file_name='dataset/Adjacency.csv'):
        self.file_name = file_name
        self.data = None

    def open(self):
        self.data = np.loadtxt(self.file_name, delimiter=',')

    def isSimilar(self, index1, index2):
        """
        checks if two index are similar
        returns True if similar
        """

        if index1 == index2:
            raise Exception('Trying to compare same indices')
        return self.data[index1, index2]
        
    



