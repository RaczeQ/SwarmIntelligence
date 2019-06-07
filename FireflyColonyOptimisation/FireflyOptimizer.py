import sys
sys.path.insert(1, '.')
from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
import logging

class FireflyOptimizer(Optimizer):

    def __init__(self, objective_function, population_size, iteration_number):
        super.__init__(objective_function, population_size, iteration_number)
       
    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        pass
        #self.particles = [Particle(self.objective_function, self.weight, self.c1, self.c2) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for i in range(len(self.iteration_number)):
            pass
            # self.find_g_best()
            # self.explore()
            