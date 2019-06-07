import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from Optimisation.Entity import Entity
import math
import logging

class Firefly(Entity):

    def __init__(self, objective_function, max_beta, absorption_coefficient):
        super().__init__(objective_function)
        self.set_entity_initial_parameters(max_beta, absorption_coefficient)
                
    def set_entity_initial_parameters(self, max_beta, absorption_coefficient):
        super().set_entity_initial_parameters()
        self.max_beta = max_beta
        self.absorption_coefficient= absorption_coefficient
        self.luminosity  =  self.fitness

    def explore_neighborhood(self, neighborhood):
        for i in range(neighborhood):
            if(neighborhood[i].luminosity > self.luminosity):
                d = math.sqrt(math.pow(self.x - neighborhood[i].x, 2) + math.pow(self.y - neighborhood[i].y, 2))
                beta = self.max_beta * math.pow(math.exp, self.absorption_coefficient * math.pow(d, 2))
                self.move_firefly(beta, neighborhood[i].x, neighborhood[i].y)        

    def move_firefly(self, beta=0, neighbor_x=0, neighbor_y=0):
        u_x, u_y = self.objective_function.sample_position()
        x, y = self.sample_position(u_x, u_y)
        self.update_position(x, y)

    def sample_position(self,  u_x, u_y, beta = 0, neighbor_x = 0, neighbor_y = 0):
        x = (1- beta) *self.x + beta *neighbor_x + u_x
        y = (1- beta) *self.y + beta *neighbor_y + u_y
        return (x, y)

    def update_position(self,  x, y):       
        try:
            new_fitness= self.evaluate_position(x, y) 
            #print(new_fitness)
            if(new_fitness >= self.fitness):
                self.x = x
                self.y = y
                self.fitness = new_fitness
            else:
                self.trial += 1
        except AssertionError:
            logging.error("The firefly was trying to escape outside the boundaries!")



                