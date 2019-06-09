from abc import ABC, abstractmethod
import numpy as np

class ObjectiveFunction(ABC):
    def __init__(self, x_min, x_max, y_min, y_max, best_pos, factor):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.best_pos = best_pos
        self.factor = factor

    def assert_boundaries(self, x, y):
        if type(x) is not type(y):
            raise TypeError('x and y have different types!')
        if type(x) in (int, float):
            assert self.x_min <= x
            assert x <= self.x_max
            assert self.y_min <= y
            assert y <= self.y_max
        else:
            assert np.all(self.x_min <= x) and np.all(x <= self.x_max)
            assert np.all(self.y_min <= y) and np.all(y <= self.y_max)

    @abstractmethod
    def evaluate(self, x, y):
        pass

    @abstractmethod
    def sample_position(self):
        pass