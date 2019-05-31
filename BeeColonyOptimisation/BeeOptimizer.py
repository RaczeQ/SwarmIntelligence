
from Optimisation.Optimizer import Optimizer
from EmployeeBee import EmployeeBee
from OnLookerBee import OnLookerBee

class BeeOptimizer(Optimizer):

    def __init__(self, objective_function, population_size, iteration_number):
        super.__init__(objective_function, population_size, iteration_number)

    def initialize_parameters(self):
        super(BeeOptimizer, self).initialize_parameters()
        self.initialize_population()

    def initialize_population(self):
        self.initialize_employees()
        self.initialize_outlookers()

    def initialize_employees(self):
        self.employeed = [EmployeeBee(self.objective_function)  for i in range(int(self.population_size/2))]


    def initialize_outlookers(self):
        self.outlookers = [OnLookerBee(self.objective_function) for  i in range(int(self.population_size/2))]



# 3 parametry: P - liczba źródeł ( populacja) , M - liczba prób tetsowych po których źródło jest wyczerpane, Cmax - maksymalna liczba cykli wykonania algorytmu

