import numpy as np
import abc
from Optimisation.Entity import Entity
class Optimizer():

    def __init__(self, objective_function, population_size, iteration_number):
        self.objective_function = objective_function
        self.population_size = population_size
        self.iteration_number = iteration_number
        self.optimal_solution = None
        self.optimal_tracing=[]
        
    
    def find_optimal_solution(self):
        self.initialize_swarm()
        self.release_the_swarm()
    
    @abc.abstractclassmethod
    def initialize_swarm(self):
        pass

    @abc.abstractclassmethod
    def release_the_swarm(self):
        pass

