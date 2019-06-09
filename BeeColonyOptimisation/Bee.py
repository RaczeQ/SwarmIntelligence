import sys
sys.path.insert(1, '.')

from Optimisation.Entity import Entity
from ObjectiveFunction.Rastrigin import Rastrigin
import logging

class Bee(Entity):

    INITIAL_PROBABILITY=0.0

    def __init__(self, objective_function):     
        super().__init__(objective_function)
        self.set_entity_initial_parameters()
            
    def set_entity_initial_parameters(self):
        super().set_entity_initial_parameters()
        self.probability = Bee.INITIAL_PROBABILITY

    def reset_bee(self):
        super().reset_entity()

    def update_position(self, x, y):
        try:
            new_fitness= self.evaluate_position(x, y) 
            if(self.factor == 1):
                if(new_fitness >= self.fitness):
                    self.set_new_position(x,y)
                    self.fitness = new_fitness
                else:
                    self.trial += 1
            else:
                if(new_fitness <= self.fitness):
                    self.set_new_position(x,y)
                    self.fitness = new_fitness
                else:
                    self.trial += 1
        except AssertionError:
            logging.error("The bee was trying to escape outside the boundaries!")



