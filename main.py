import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

from ObjectiveFunction import Rastrigin

dx, dy = 0.05, 0.05

# generate 2 2d grids for the x & y bounds
y, x = np.mgrid[slice(-5, 5 + dy, dy),
                slice(-5, 5 + dx, dx)]

R = Rastrigin(-5, 5, -5, 5)

z = [[R.evaluate(x,y) for x in ]]
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())