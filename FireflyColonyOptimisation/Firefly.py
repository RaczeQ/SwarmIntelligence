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
        for i in range(len(neighborhood)):
            if(self.factor>1):
                if(neighborhood[i].luminosity > self.luminosity):
                    self.move_forward(neighborhood[i])       
            else:
                if(neighborhood[i].luminosity < self.luminosity):
                   self.move_forward(neighborhood[i])

    def move_forward(self, neighbor):
        d = math.sqrt(math.pow(self.x - neighbor.x, 2) + math.pow(self.y - neighbor.y, 2))
        power = -self.absorption_coefficient * math.pow(d, 2)
        beta = self.max_beta * math.exp(power)
        self.move_firefly(beta, neighbor.x, neighbor.y)   

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
            new_luminosity =  self.evaluate_position(x, y) 
            if(self.factor>1):
                if(new_luminosity >= self.luminosity):
                    self.set_new_position(x,y)
                    self.luminosity = new_luminosity
                else:
                    self.trial += 1
            else:
                if(new_luminosity <= self.luminosity):
                    self.set_new_position(x,y)
                    self.luminosity = new_luminosity
                else:
                    self.trial += 1
        except AssertionError:
            logging.error("The firefly was trying to escape outside the boundaries!")



                