import math
import random
import numpy as np

from .ObjectiveFunction import ObjectiveFunction


class Bukin6(ObjectiveFunction):
    def __init__(self, x_min=-15, x_max=5, y_min=-3, y_max=3):
        super().__init__(x_min, x_max, y_min, y_max, (-10, 1), -1)
    
    def evaluate(self, x, y):
        val = 100 * np.sqrt(np.abs(y - 0.01 * x ** 2)) + 0.01 + np.abs(x + 10)
        return -val
    
    def sample_position(self):
        x = self.x_min + random.uniform(0, 1)*(self.x_max - self.x_min)
        y = self.y_min + random.uniform(0, 1)*(self.y_max - self.y_min)
        return (x, y)