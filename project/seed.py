import numpy as np

class Seed():
    
    def __init__(self, file_name='dataset/seed.csv'):
        self.file_name = file_name
        self.data = None
        self.open()

    def open(self):
        self.data = np.loadtxt(self.file_name, delimiter=',')

    def get_digit(self, digit, index=None):
        """ returns indices -1 """
        if not index:
            return (self.data[digit]-1)
        else:
            return (self.data[digit][index]-1)

    def get_data(self, feature_data, index=None):
        """ Return array of all training data set"""
        seed_data = np.ndarray([])
        for i in range(10):
            digit = self.get_digit(i)

            for j in range(3):
                d = feature_data[int(digit[j])]
                if i==0 and j==0:
                    seed_data = d
                else:
                    seed_data = np.vstack((seed_data, d))

        return seed_data
    
    def print_arr(self, feature_data):
        answer = []
        current_digit = 0
        n_times = 0
        
        for i in range(len(feature_data)):
            if n_times == 3:
                current_digit += 1
                n_times=0
                print "\n"*2
            print "Digit {} = val: {}".format(current_digit, feature_data[i])
            n_times += 1
        return answer
