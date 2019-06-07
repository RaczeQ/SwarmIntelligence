import sys
sys.path.insert(1, '.')


from Optimisation.Optimizer import Optimizer
from EmployeeBee import EmployeeBee
from OnLookerBee import OnLookerBee
from ObjectiveFunction.Rastrigin import Rastrigin
import numpy as np
import logging
class BeeOptimizer(Optimizer):

    def __init__(self, objective_function, population_size, iteration_number, max_trials):
        super().__init__(objective_function, population_size, iteration_number)
        self.max_trials = max_trials

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
            self.check_optimal_solution()
            
    def explore(self):
        self.make_employee_bees_working()

    def calculate_probabilities(self):
        max_fitness =  max(e.fitness for e in self.employeed) 
        print("The best fitness: "+str(max_fitness)) 
        for i in range(len(self.employeed)):
            self.employeed[i].count_probability(max_fitness)

    def find_best_bees(self):
        max_prob = max(e.probability for e in self.employeed)
        best_bee = list(filter(lambda b: b.probability == max_prob, self.employeed))
        self.best_bees = best_bee
        
      #  print("The best bee, prob: "+str(max_prob))

    def onlook(self):
        self.make_onlooker_bees_working()

    def check_optimal_solution(self):
        # tracing
        pass

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

#test
o = Rastrigin(0.,100.,0.,200., 1.)
b=BeeOptimizer(o, 50, 100, 6)
b.initialize_swarm()
b.release_the_swarm()


# 3 parametry: P - liczba źródeł ( populacja) , M - liczba prób tetsowych po których źródło jest wyczerpane, Cmax - maksymalna liczba cykli wykonania algorytmu

