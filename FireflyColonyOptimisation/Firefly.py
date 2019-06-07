import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from Optimisation.Entity import Entity

class Firefly(Entity):

    def __init__(self, objective_function, beta, max_beta, absorption_coefficient):
        super().__init__(objective_function)
        
        
    def set_entity_initial_parameters(self, beta, max_beta, absorption_coefficient):
        super().set_entity_initial_parameters()
        self.beta = beta
        self.max_beta = max_beta
        self.absorption_coefficient= absorption_coefficient
        #self.luminosity  = odwrotność funkcji kosztu
        