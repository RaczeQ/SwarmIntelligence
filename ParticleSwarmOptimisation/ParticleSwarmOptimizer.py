import sys
sys.path.insert(1, '.')
from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
import logging

class ParticleSwarmOptimizer(Optimizer):

    def __init__(self, objective_function, population_size, iteration_number, weight, c1, c2):
        super.__init__(objective_function, population_size, iteration_number)
        self.g_best_particle = None
        self.weight = weight
        self.c1 = c1
        self.c2 = c2

    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.particles = [Particle(self.objective_function, self.weight, self.c1, self.c2) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for i in range(len(self.iteration_number)):
            self.find_g_best()
            self.explore()
            
    def find_g_best(self):
        max_prob = max(e.fitness for e in self.particles)
        self.g_best_particle = list(filter(lambda b: b.fitness == max_prob, self.particles))
        
    def explore(self):
        for i in range(len(self.particles)):
            try:
                self.particles[i].explore_neighborhood(self.g_best_particle)
            except AssertionError:
                logging.error("The particle was trying to escape outside the boundaries!")



