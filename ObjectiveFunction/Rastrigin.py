import math
import random
import numpy as np

from .ObjectiveFunction import ObjectiveFunction


class Rastrigin(ObjectiveFunction):
    def __init__(self, x_min, x_max, y_min, y_max, A = 10):
        self.A = A
        super().__init__(x_min, x_max, y_min, y_max)
    
    def evaluate(self, x, y):
        # assert x >= self.x_min and x <= self.x_max
        # assert y >= self.y_min and y <= self.y_max
        return self.A + (x**2 - self.A * np.cos(2 * math.pi * x)) + (y**2 - self.A * np.cos(2 * math.pi * y))
    
    def sample_position(self):
        x = self.x_min + random.uniform(0, 1)*(self.x_max - self.x_min)
        y = self.y_min + random.uniform(0, 1)*(self.y_max - self.y_min)
        return (x, y)