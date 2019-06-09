import os

import numpy as np
import pandas as pd
import abc
from Optimisation.Entity import Entity
class Optimizer():

    def __init__(self, objective_function, population_size, iteration_number, result_file_name):
        self.objective_function = objective_function
        self.population_size = population_size
        self.iteration_number = iteration_number
        self.optimal_solution = None
        self.optimal_tracing=[]
        self.result_file_name = result_file_name
        self.factor = objective_function.factor
        
    
    def find_optimal_solution(self):
        self.initialize_swarm()
        self.release_the_swarm()
    
    @abc.abstractclassmethod
    def initialize_swarm(self):
        pass

    @abc.abstractclassmethod
    def release_the_swarm(self):
        pass

    def save_optimal_tracing(self, configuration):
        file_path = os.path.join('results', f'{self.result_file_name}.txt')
        keys = list(configuration.keys())
        values = list(configuration.values())   
        keys.append('best_fitness')
        v = np.repeat(np.reshape(np.asarray(values), (-1, 1)).T, len(self.optimal_tracing), axis = 0)
        s =np.reshape(np.asarray(self.optimal_tracing), (-1, 1))
        result = np.concatenate((v, s), axis=1)
        df = pd.DataFrame()
        try:
            df = pd.read_csv(file_path, index_col=0) 
        except:
            df = pd.DataFrame(columns=keys)
        row =pd.DataFrame( result, columns=keys)
        df = pd.concat ([df, row], axis=0, ignore_index=True) 
        df.to_csv(file_path)

    def save_animation(self, file_name):
        self.plotter.save_animation(file_name)
