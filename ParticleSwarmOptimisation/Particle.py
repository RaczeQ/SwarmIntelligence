import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from Optimisation.Entity import Entity
import random


class Particle(Entity):

    def __init__(self, objective_function, weight, c1, c2):
        super().__init__(objective_function)
        self.set_entity_initial_parameters(weight, c1, c2)
        
    def set_entity_initial_parameters(self, weight, c1, c2):
        super().set_entity_initial_parameters()
        self.weight = weight
        self.c1 = c1
        self.c2 = c2
        self.p_best_x = self.x
        self.p_best_y = self.y
        self.p_best_fitness = self.fitness
        self.velocity_x, self.velocity_y = self.objective_function.sample_position()

    def explore_neighborhood(self, neighborhood):
        x, y = self.sample_new_position(neighborhood)
        self.update_position(x, y)
        self.update_p_best()
       
    def sample_new_position(self, neighborhood):
        bests = len(neighborhood)
        sampled_best = random.randint(0, bests-1)
        self.velocity_x = self.weight*self.velocity_x + self.c1 * random.uniform(0, 1) * (self.p_best_x - self.x) + self.c2 * random.uniform(0, 1) * (neighborhood[sampled_best].velocity_x)
        self.velocity_y = self.weight*self.velocity_y + self.c1 * random.uniform(0, 1) * (self.p_best_y - self.y) + self.c2 * random.uniform(0, 1) * (neighborhood[sampled_best].velocity_y)
        return (self.velocity_x + self.x, self.velocity_y + self.y)

    def update_position(self, x, y):
        self.fitness = self.evaluate_position(x, y)
        self.x = x
        self.y = y

    def update_p_best(self):
        if(self.factor >0):
            if(self.p_best_fitness <= self.fitness):
                self.p_best_x = self.x
                self.p_best_y = self.y
                self.p_best_fitness = self.fitness
                self.set_new_position(self.p_best_x,self.p_best_y)
        else:
            if(self.p_best_fitness >= self.fitness):
                self.p_best_x = self.x
                self.p_best_y = self.y
                self.p_best_fitness = self.fitness
                self.set_new_position(self.p_best_x,self.p_best_y)

       
