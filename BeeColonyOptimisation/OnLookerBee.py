from BeeColonyOptimisation.Bee import Bee
import numpy as np
import random
class OnLookerBee(Bee):
    
    def onlook(self,  best_bees, max_trial):
        candidate = np.random.choice(best_bees)
        self.exploite_position(candidate.x, candidate.y, candidate.fitness, max_trial)

    def exploite_position(self, x, y,  fitness, max_trial):
        if(self.trial < max_trial):
            sampled_x, sampled_y = self.sample_new_position(x, y)
            self.update_position(sampled_x, sampled_y)


    def sample_new_position(self, neighbor_x, neighbor_y):
        coordinates = ['x', 'y']
        choice = random.choice(coordinates)
        if(choice=='x'):
            return ( self.x + random.uniform(-1, 1)* (self.x - neighbor_x), self.y)
        else:
            return ( self.x , self.y + random.uniform(-1, 1)* (self.y - neighbor_y))