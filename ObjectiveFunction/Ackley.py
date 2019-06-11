import math
import random
import numpy as np

from .ObjectiveFunction import ObjectiveFunction


class Ackley(ObjectiveFunction):
    def __init__(self, x_min=-4, x_max=4, y_min=-4, y_max=4, a=20, b=0.2, c=2*np.pi):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(x_min, x_max, y_min, y_max, (0,0), -1)
    
    def evaluate(self, x, y):
        self.assert_boundaries(x, y)
        val = -self.a*np.exp(-self.b*np.sqrt(0.5*(x**2 + y**2))) - np.exp(0.5*(np.cos(self.c*x) + np.cos(self.c*y))) + self.a + np.exp(1.0)
        return val
    
    def sample_position(self):
        x = self.x_min + random.uniform(0, 1)*(self.x_max - self.x_min)
        y = self.y_min + random.uniform(0, 1)*(self.y_max - self.y_min)
        return (x, y)