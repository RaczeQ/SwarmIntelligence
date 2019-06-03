import sys
sys.path.insert(1, '.')


from Optimisation.Optimizer import Optimizer
from EmployeeBee import EmployeeBee
from OnLookerBee import OnLookerBee
from ObjectiveFunction.Rastrigin import Rastrigin
import numpy as np
class BeeOptimizer(Optimizer):

    def __init__(self, objective_function, population_size, iteration_number, max_trials):
        super().__init__(objective_function, population_size, iteration_number)
        self.max_trials = max_trials
        self.the_best_found_solutions=[]
        self.sources=[]      

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
            self.make_onlooker_bees_working()

    def explore(self):
        self.make_employee_bees_working()
        
    def make_employee_bees_working(self):
        neighborhood = self.get_neighborhood_positions()
        for i in range(len(self.employeed)):
            copy = neighborhood.copy()
            copy.pop(i)
            self.employeed[i].explore_neighborhood(copy)

    def get_neighborhood_positions(self):
        return [ [self.employeed[i].x, self.employeed[i].y] for i in range(len(self.employeed)) ]


    def calculate_probabilities(self):
        max_fitness =  max(e.fitness for e in self.employeed)   
        for i in range(len(self.employeed)):
            self.employeed[i].count_probability(max_fitness)

    def find_best_bees(self):
        max_prob = max(e.probability for e in self.employeed)
        best_bee = list(filter(lambda b: b.probability == max_prob, self.employeed))
        self.best_bees = best_bee

    def make_onlooker_bees_working(self):
        for i in range(len(self.outlookers)):
            self.outlookers.onlook(self.best_bees, self.max_trials)


#test
o = Rastrigin(0.,100.,0.,200., 1.)
b=BeeOptimizer(o, 10, 10, 6)
b.initialize_swarm()
b.release_the_swarm()


# 3 parametry: P - liczba źródeł ( populacja) , M - liczba prób tetsowych po których źródło jest wyczerpane, Cmax - maksymalna liczba cykli wykonania algorytmu

