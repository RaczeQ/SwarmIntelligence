
from SwarmOptimizer import SwarmOptimizer
from BeeColony.EmployeeBee import EmployeeBee
from BeeColony.OnLookerBee import OnLookerBee

class BeeOptimizer(SwarmOptimizer):


    def initialize_population(self):
        self.initialize_employees()
        self.initialize_outlookers()

    def initialize_employees(self):
        self.employeed = [EmployeeBee(self.objective_function)  for i in range(int(self.population_size/2))]


    def initialize_outlookers(self):
        self.outlookers = [OnLookerBee(self.objective_function) for  i in range(int(self.population_size/2))]

