#import matplotlib.pyplot as plt
import numpy as np

colors = 100*['black', 'sienna', 'tan',
            'gold', 'dodgerblue', 'darkblue',
            'hotpink', 'pink', 'green',
            'r']

#colors = 20 * ['b']
#colors = 10*['r', 'g', 'b', 'c', 'k', 'y', 'm']
def make_digit_arr(n_times=3, limit=10):
    arr = np.arange(limit)
    arr = arr.repeat(n_times)
    return arr

def plot_2d(plt, X, Y, marker='o', size='o', color_label=None):
    """    
    """
    if not color_label:
        color_label = np.zeros(len(X))
    for i in range(len(X)):        
        plt.scatter(X,Y, c = colors[i%10], marker=marker, s=size)

    return plt
