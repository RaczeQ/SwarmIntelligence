import numpy as np
from ObjectiveFunction.ObjectiveFunction import ObjectiveFunction


class SwarmOptimizer():
    def __init__(self, population_size, iteration_num, max_tials, objective_function):
        self.population_size= population_size
        self.iteration_num =iteration_num
        self.max_tials = max_tials
        self.objective_function = objective_function
       
        self.optimal_solution = None
        self.the_best_found_solutions=[]
        self.sources=[]
        
    def initialize_population(self):
        pass

  
    def initialize_sources(self):
        self.sample_initial_positions()
    

      #inicjujemy współrzędne poczatkowych położeń z losowymi wartościami
    def sample_initial_positions(self):
        self.sources = np.random.rand(self.population_size, len(self.objective_function.dimention))
        self.sources = [[ (self.sources[:, i].min() + i * (self.sources[:, i].max() - self.sources[:, i].min())) for i in range(len(self.objective_function.dimention))] for j in range(self.population_size)]

    