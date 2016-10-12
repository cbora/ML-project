from project.seed import Seed
from project.feature import Feature
import matplotlib.pyplot as plt
import numpy as np

# Get all features
f = Feature()

all_data = f.get_data()


# compute variance of all features
var = np.var(all_data, axis=0)

print "max: ", np.max(var)
print "min: ", np.min(var)

plt.hist(var, histtype='bar')

plt.xlabel('Variance')
plt.ylabel('Frequency')

plt.title('Variance distribution')
plt.show()

