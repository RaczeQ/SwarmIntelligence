import math
import random
import numpy as np

from .ObjectiveFunction import ObjectiveFunction


class Sphere(ObjectiveFunction):
    def __init__(self, x_min=-5, x_max=5, y_min=-5, y_max=5):
        super().__init__(x_min, x_max, y_min, y_max, (0,0), -1)
    
    def evaluate(self, x, y):
        self.assert_boundaries(x, y)
        val = x**2 + y**2
        return val
    
    def sample_position(self):
        x = self.x_min + random.uniform(0, 1)*(self.x_max - self.x_min)
        y = self.y_min + random.uniform(0, 1)*(self.y_max - self.y_min)
        return (x, y)