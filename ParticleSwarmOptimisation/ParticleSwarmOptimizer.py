import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
class ParticleSwarmOptimizer(Optimizer):

     def __init__(self, objective_function, population_size, iteration_number):
        super.__init__(objective_function, population_size, iteration_number)
        self.g_best_x = -1
        self.g_best_y = -1
        self.g_best_fitness = -1
      
    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.particles = [Optimizer(self.objective_function) for i in range(int(self.population_size))]


    def release_the_swarm(self):
        for i in range(len(self.iteration_number)):
            self.find_g_best()
            self.explore()
            
    def find_g_best():
        # max_prob = max(e.probability for e in self.employeed)
        # best_bee = list(filter(lambda b: b.probability == max_prob, self.employeed))


    def explore():
        for i in range(len(self.particles)):
            self.particles[i].explore_neighborhood(None)



