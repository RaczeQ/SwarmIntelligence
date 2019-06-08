import math
import random
import numpy as np

from .ObjectiveFunction import ObjectiveFunction


class Trid(ObjectiveFunction):
    def __init__(self, x_min=-4, x_max=4, y_min=-4, y_max=4):
        super().__init__(x_min, x_max, y_min, y_max, -1)
    
    def evaluate(self, x, y):
        return (x-1)**2 + (y-1)**2 - x*y
    
    def sample_position(self):
        x = self.x_min + random.uniform(0, 1)*(self.x_max - self.x_min)
        y = self.y_min + random.uniform(0, 1)*(self.y_max - self.y_min)
        return (x, y)