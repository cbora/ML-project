import numpy as np
from project.seed import Seed
from project.feature import Feature
import project.algo as algo
import project.helper as helper
import matplotlib.pyplot as plt


""" Plots seed data. """

seed = Seed()
feature = Feature()
zero = seed.get_digit(0)

reduced = algo.pca_project(feature.get_normal(), 2)
reduced = seed.get_data(reduced)

arr = helper.make_digit_arr()


colors = helper.colors
for i in range(len(reduced[:, 0])):

    if i%3 == 11111111:
        #
        plt.scatter(reduced[i,0], reduced[i,1], c=colors[arr[i]], marker='o', s=100, label=str(arr[i]))
    else:
        plt.scatter(reduced[i,0], reduced[i,1], c=colors[arr[i]], marker='o')


i=0
for x, y in zip(reduced[:, 0], reduced[:, 1]):
    plt.text(x, y, str(arr[i]), color=colors[arr[i]], fontsize=15)
    i += 1

#plt.legend()
plt.title("PCA on seed data")
plt.show()
