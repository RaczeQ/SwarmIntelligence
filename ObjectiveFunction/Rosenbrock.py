import math
import random
import numpy as np

from .ObjectiveFunction import ObjectiveFunction


class Rosenbrock(ObjectiveFunction):
    def __init__(self, x_min=-2, x_max=2, y_min=-1, y_max=3, a=1, b=100):
        self.a = a
        self.b = b
        super().__init__(x_min, x_max, y_min, y_max, (self.a, self.a**2), -1)
    
    def evaluate(self, x, y):
        val = (self.a - x)**2 + self.b*(y - x**2)**2
        return -val
    
    def sample_position(self):
        x = self.x_min + random.uniform(0, 1)*(self.x_max - self.x_min)
        y = self.y_min + random.uniform(0, 1)*(self.y_max - self.y_min)
        return (x, y)