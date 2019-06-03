import sys
sys.path.insert(1, '.')

from Optimisation.Entity import Entity
from ObjectiveFunction.Rastrigin import Rastrigin


class Bee(Entity):
    def __init__(self, objective_function):     
        super().__init__(objective_function)
   
    def set_entity_initial_parameters(self):
        super().set_entity_initial_parameters()
        self.probability = 0.0

    def reset_bee(self):
        self.set_entity_initial_parameters()


    # def find_candidate_solution(self):
    #     dim = self.sample_dimention()
    #     neighbor = self.sample_neighbor()
    #     return  np.random.rand() 
      
    # def sample_dimention():
    #     pass

    # def sample_neighbor():
    #     pass

#test
o = Rastrigin(2.,10.,5.,60., 1.)
b=Bee(o)


