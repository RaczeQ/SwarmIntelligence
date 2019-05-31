import numpy as np

class Optimizer():

    def __init__(self, objective_function, population_size, iteration_number):
        self.objective_function = objective_function
        self.population_size = population_size
        self.iteration_number = iteration_number

        self.optimal_solution = None
        self.the_best_found_solutions=[]
        self.sources=[]
        
    
    def initialize_parameters(self):
        self.initialize_positions()


    def evaluate_position_values(self):
        pass

    def initialize_positions(self):
        self.sources = np.random.rand(self.population_size, len(self.objective_function.dimention))
        self.sources = [[ (self.sources[:, i].min() + i * (self.sources[:, i].max() - self.sources[:, i].min())) for i in range(len(self.objective_function.dimention))] for j in range(self.population_size)]

    