

import scipy.io

fname = "test_data.mat"
data = scipy.io.loadmat(fname)

import matplotlib
matplotlib.use("MacOSX")
import matplotlib.pyplot as plt

X = data['X']
Y = data['Y']
Z = data['Z']

plt.imshow(Z)
plt.hot()
plt.colorbar()
plt.show()

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = Axes3D(fig)
ax.plot_surface(X,Y,Z, cmap=cm.hot)
plt.show()




