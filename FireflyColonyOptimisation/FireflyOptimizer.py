import sys
sys.path.insert(1, '.')
from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
from FireflyColonyOptimisation.Firefly import Firefly
import logging

class FireflyOptimizer(Optimizer):

    def __init__(self, objective_function, population_size, iteration_number,  max_beta, absorption_coefficient):
        super.__init__(objective_function, population_size, iteration_number)
        self.max_beta = max_beta
        self.absorption_coefficient = absorption_coefficient
       
    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.firefly = [Firefly(self.objective_function, self.max_beta, self.absorption_coefficient) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for k in range(len(self.iteration_number)):
            for i in range(len(self.population_size)):
                for j in range(i):
                    if(i!=j):
                        self.firefly.explore_neighborhood(self.firefly[:i])
                    else:
                        self.firefly.move_firefly()
            