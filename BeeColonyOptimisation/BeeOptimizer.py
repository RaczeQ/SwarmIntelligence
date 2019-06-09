import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from EmployeeBee import EmployeeBee
from OnLookerBee import OnLookerBee
from ObjectiveFunction import Rastrigin, Bukin6, Rosenbrock
import numpy as np
import logging
from Plotter import Plotter


class BeeOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name, skip_frames=0):
        super().__init__(objective_function, configuration[0], configuration[1] ,result_file_name)
        self.max_trials = configuration[2]
        self.skip_frames = skip_frames
        self.plotter = Plotter(objective_function, 'Bees')

    def initialize_swarm(self):
        self.initialize_population()

    def initialize_population(self):
        self.initialize_employees()
        self.initialize_outlookers()

    def initialize_employees(self):
        self.employeed = [EmployeeBee(self.objective_function, self.max_trials)  for i in range(int(self.population_size/2))]

    def initialize_outlookers(self):
        self.outlookers = [OnLookerBee(self.objective_function) for  i in range(int(self.population_size/2))]

    def release_the_swarm(self):
        for i in range(self.iteration_number):
            self.explore()
            self.calculate_probabilities()
            self.find_best_bees()
            self.onlook()
            self.update_optimal_solution_tracking()
            if self.skip_frames == 0 or i % self.skip_frames == 0:
                self.plotter.add_frame(i, self.employeed + self.outlookers)
            print(i)
        self.plotter.add_frame(self.iteration_number, self.employeed + self.outlookers)
            
    def explore(self):
        self.make_employee_bees_working()

    def calculate_probabilities(self):
        sum_fitness = sum(x.fitness for x in self.employeed)
        for i in range(len(self.employeed)):
            self.employeed[i].count_probability(sum_fitness)

    def find_best_bees(self):
        if(self.factor == 1):
            prob = max(e.probability for e in self.employeed)
        else:
            prob = min(e.probability for e in self.employeed)
        best_bee = list(filter(lambda b: b.probability == prob, self.employeed))
        self.best_bees = best_bee

    def onlook(self):
        self.make_onlooker_bees_working()

    def update_optimal_solution_tracking(self):
        if(self.factor == 1):
            fitness =  max(e.fitness for e in self.outlookers) 
        else:
            fitness =  min(e.fitness for e in self.outlookers) 
        self.optimal_tracing.append(fitness)

    def make_employee_bees_working(self):
        neighborhood = self.get_neighborhood_positions()
        for i in range(len(self.employeed)):
            copy = neighborhood.copy()
            copy.pop(i)
            self.employeed[i].explore_neighborhood(copy)
        
    def get_neighborhood_positions(self):
        return [ [self.employeed[i].x, self.employeed[i].y] for i in range(len(self.employeed)) ]

    def make_onlooker_bees_working(self):
        for i in range(len(self.outlookers)):
            self.outlookers[i].onlook(self.best_bees, self.max_trials)

    def save_state(self, file_name, line_history):
        self.plotter.save_state_to_file(file_name, self.employeed + self.outlookers, line_history)

#test
fn = 'bee'
o = Rosenbrock()

configuration_settings={'population_size': 100,
                'iteration_number': 300,
                'max_trials' : 5}

configuration = list(configuration_settings.values())
b=BeeOptimizer(o, configuration, fn, 10)

b.initialize_swarm()
b.release_the_swarm()
b.save_optimal_tracing(configuration_settings)
b.save_animation('bees')
b.save_state('bees_hist', False)
# False - historia nie wygląda zbyt ładnie jeszcze

# 3 parametry: P - liczba źródeł ( populacja) , M - liczba prób tetsowych po których źródło jest wyczerpane, Cmax - maksymalna liczba cykli wykonania algorytmu

