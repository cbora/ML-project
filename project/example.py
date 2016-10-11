import numpy as np
from seed import Seed
from feature import Feature
import algo
import helper
import matplotlib.pyplot as plt


""" A dirty starter exmple script. """

seed = Seed()
feature = Feature()
zero = seed.get_digit(0)
seed_data = []

for i in range(10):

    digit = seed.get_digit(i)

    for j in range(3):
        data = feature.get_digit(int(digit[j]))
        seed_data.append(data)
        print "Digit {}  =  var: {} mean: {}".format(i, np.var(data), np.mean(data))
    print "\n" *2

print len(seed_data)

print seed_data[0]
print seed_data[0].shape

clusters, _, _ = algo.kmeans(seed_data, K=10)

sl_cluster, _ = algo.singlelink(seed_data, K=10)
ans = seed.print_arr(clusters)

print "---"*30
print "\n"*4
ans2 = seed.print_arr(sl_cluster)



d_data = feature.get_data()
m_data = feature.get_centered()
#reduced = algo.randomprojection_project(feature.get_data(), 2)
#reduced = algo.pca_project(feature.get_centered(), 2)
reduced = algo.pca_project(feature.get_normal(), 2)
#reduced = algo.pca_project(feature.get_data(), 2)
#reduced = algo.pca_project(seed_data, 2)
#reduced = algo.pca_project(seed.get_data(feature.get_data()), 2)
#print seed.get_digit(0)
reduced = seed.get_data(reduced)
print reduced.shape
arr = helper.make_digit_arr()

print len(arr)
print arr
#helper.plot_2d(plt, reduced[:,0], reduced[:,1], color_label=arr)
colors = helper.colors
for i in range(len(reduced[:, 0])):
    #plt.scatter(reduced[i,0], reduced[i,1], c=colors[i%10], marker='o', s=100)

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
