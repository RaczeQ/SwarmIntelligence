import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from Optimisation.Entity import Entity


class Particle(Entity):

    def __init__(self, velocity, objective_function):
        super().__init__(objective_function)
        

    def set_entity_initial_parameters(self, velocity):
        super().set_entity_initial_parameters()
        self.velocity = velocity
        self.p_best_x = self.x
        self.p_best_y = self.y
        self.p_best_fitness = self.fitness

    def explore_neighborhood(self, neighborhood):
        x, y = self.sample_new_position(neighborhood)
        self.update_position(x, y)
        self.update_p_best()
       
    def sample_new_position(self, neighborhood):
        return (0,0)

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.fitness = self.evaluate_position(x, y)
        
    def update_p_best(self):
        if(self.p_best_fitness < self.fitness):
            self.p_best_x = self.x
            self.p_best_y = self.y
            self.p_best_fitness = self.fitness

       
