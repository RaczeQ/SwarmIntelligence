import sys
sys.path.insert(1, '.')

from Optimisation.Entity import Entity
from ObjectiveFunction.Rastrigin import Rastrigin


class Bee(Entity):

    INITIAL_PROBABILITY=0.0

    def __init__(self, objective_function):     
        super().__init__(objective_function)
        
    def set_entity_initial_parameters(self):
        super().set_entity_initial_parameters()
        self.probability = Bee.INITIAL_PROBABILITY

    def reset_bee(self):
        self.set_entity_initial_parameters()

#test
o = Rastrigin(2.,10.,5.,60., 1.)
b=Bee(o)


