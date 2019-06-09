import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
from ObjectiveFunction.Rastrigin import Rastrigin
from Plotter import Plotter
import logging

class ParticleSwarmOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name):
        super().__init__(objective_function, configuration[0], configuration[1], result_file_name)
        self.g_best_particle = None
        self.weight = configuration[2]
        self.c1 = configuration[3]
        self.c2 = configuration[4]
        self.plotter = Plotter(objective_function, 'PSO')

    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.particles = [Particle(self.objective_function, self.weight, self.c1, self.c2) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for i in range(self.iteration_number):
            self.find_g_best()
            self.explore()
            self.update_optimal_solution_tracking()
            self.plotter.add_frame(i, self.particles)
            print(i)
            
    def find_g_best(self):
        if self.factor > 0:
            max_prob = max(e.fitness for e in self.particles)
        else:
            max_prob = min(e.fitness for e in self.particles)
        self.g_best_particle = list(filter(lambda b: b.fitness == max_prob, self.particles))
        
    def explore(self):
        for i in range(len(self.particles)):
            try:
                self.particles[i].explore_neighborhood(self.g_best_particle)
            except AssertionError:
                logging.error("The particle was trying to escape outside the boundaries!")

    def update_optimal_solution_tracking(self):
        if self.factor > 0:
            fitness =  max(e.fitness for e in self.particles) 
        else:
            fitness =  min(e.fitness for e in self.particles) 
        self.optimal_tracing.append(fitness)

    def save_state(self, file_name, line_history):
        self.plotter.save_state_to_file(file_name, self.particles, line_history)

#test
fn = 'particle'
o = Rastrigin()

configuration_settings={'population_size': 10,
                'iteration_number': 50,
                'weight' : 0.6,
                'c1': 0.6,
                'c2': 0.2}

configuration = list(configuration_settings.values())
b=ParticleSwarmOptimizer(o, configuration, fn)

b.initialize_swarm()
b.release_the_swarm()
b.save_optimal_tracing(configuration_settings)
b.save_animation('pso')
b.save_state('pso_hist', False)
# False - historia nie wygląda zbyt ładnie jeszcze