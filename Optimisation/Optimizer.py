import numpy as np
import abc
from Optimisation.Entity import Entity
class Optimizer():

    def __init__(self, objective_function, population_size, iteration_number):
        self.objective_function = objective_function
        self.population_size = population_size
        self.iteration_number = iteration_number
        self.optimal_solution = None
        self.the_best_found_solutions=[]
        self.sources=[]      
        
    
    def find_optimal_solution(self):
        self.initialize_swarm()
        self.release_the_swarm()
    
    @abc.abstractclassmethod
    def initialize_swarm(self):
        pass

    @abc.abstractclassmethod
    def release_the_swarm(self):
        pass



    # def initialize_parameters(self):
    #     pass
    #     #self.initialize_positions()

    # def evaluate_position_values(self):
    #     pass


    # @abc.abstractclassmethod
    # def initialize_positions(self):
    #     pass
    #     # self.sources = np.random.rand(self.population_size, len(self.objective_function.dimention))
    #     # self.sources = [[ (self.sources[:, i].min() + i * (self.sources[:, i].max() - self.sources[:, i].min())) for i in range(len(self.objective_function.dimention))] for j in range(self.population_size)]

    