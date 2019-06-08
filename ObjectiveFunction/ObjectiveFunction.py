from abc import ABC, abstractmethod

class ObjectiveFunction(ABC):
    def __init__(self, x_min, x_max, y_min, y_max, best_pos, factor):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.best_pos = best_pos
        self.factor = factor

    @abstractmethod
    def evaluate(self, x, y):
        pass

    @abstractmethod
    def sample_position(self):
        pass