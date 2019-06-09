from BeeColonyOptimisation.Bee import Bee
import random
class EmployeeBee(Bee):
    
    def __init__(self, objective_function, max_trials):
        super().__init__(objective_function)
        self.max_trials = max_trials


    def explore_neighborhood(self, neighborhood):
        if(self.trial < self.max_trials):
            x, y = self.sample_new_position(neighborhood)
            self.update_position(x, y)
        else:
            super().reset_bee()
            x, y = self.sample_new_position(neighborhood)
            self.update_position(x, y)
          
    def sample_new_position(self, neighborhood):
        coordinates = ['x', 'y']
        choice = random.choice(coordinates)
        neighbor = random.randint(0, len(neighborhood)-1)
        chosen_index = neighborhood[neighbor]
        if(choice=='x'):
            return ( self.x + random.uniform(-1, 1)* (self.x - chosen_index[0]), self.y)
        else:
            return ( self.x , self.y + random.uniform(-1, 1)* (self.y - chosen_index[1]))


    def count_probability(self, all_fitness):
        self.probability = self.fitness / all_fitness