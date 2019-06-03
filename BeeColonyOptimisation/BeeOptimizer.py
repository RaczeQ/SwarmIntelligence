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

    def initialize_swarm(self):
        self.initialize_population()
        #self.initialize_sources()

    def initialize_population(self):
        self.initialize_employees()
        self.initialize_outlookers()

    def initialize_employees(self):
        self.employeed = [EmployeeBee(self.objective_function, self.max_trials)  for i in range(int(self.population_size/2))]

    def initialize_outlookers(self):
        self.outlookers = [OnLookerBee(self.objective_function) for  i in range(int(self.population_size/2))]

    # def initialize_sources(self):
    #     self.sources = np.random.rand(self.population_size, len(self.objective_function.dimention))
    #     self.sources = [[ (self.sources[:, j].min() + i * (self.sources[:, j].max() - self.sources[:, j].min())) for i in range(len(self.objective_function.dimention))] for j in range(self.population_size)]

    def release_the_swarm(self):
        for i in range(self.iteration_number):
            self.make_employee_bees_working()
            self.make_outlooker_bees_working()

    def make_employee_bees_working(self):
        neighborhood = self.get_neighborhood_positions()
        for i in range(len(self.employeed)):
            copy = neighborhood.copy()
            copy.pop(i)
            self.employeed[i].explore_neighborhood(copy)

    def get_neighborhood_positions(self):
        return [ [self.employeed[i].x, self.employeed[i].y] for i in range(len(self.employeed)) ]

    def make_outlooker_bees_working(self):
        for i in range(len(self.outlookers)):
            pass


#test
o = Rastrigin(2.,10.,5.,60., 1.)
b=BeeOptimizer(o, 10, 10, 6)
b.initialize_swarm()
b.make_employee_bees_working()

# 3 parametry: P - liczba źródeł ( populacja) , M - liczba prób tetsowych po których źródło jest wyczerpane, Cmax - maksymalna liczba cykli wykonania algorytmu

