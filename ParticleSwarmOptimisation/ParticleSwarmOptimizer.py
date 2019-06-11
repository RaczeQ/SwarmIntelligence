import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
from ObjectiveFunction.Rastrigin import Rastrigin
from Plotter import Plotter
import logging
import numpy as np
class ParticleSwarmOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name, skip_frames=0):
        super().__init__(objective_function, configuration[0], configuration[1], result_file_name)
        self.g_best_particle = None
        self.weight = configuration[2]
        self.c1 = configuration[3]
        self.c2 = configuration[4]
        self.skip_frames = skip_frames
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
            if self.skip_frames == 0 or i % self.skip_frames == 0:
                self.plotter.add_frame(i, self.particles)
            print(i)
        self.plotter.add_frame(self.iteration_number, self.particles)
            
    def find_g_best(self):
        if self.factor > 0:
            fitness = max(e.p_best_fitness for e in self.particles)
        else:
            fitness = min(e.p_best_fitness for e in self.particles)
        print('the best fit ===================> '+str(fitness))
        self.g_best_particle = list(filter(lambda b: b.p_best_fitness == fitness, self.particles))
        self.optimal_solution.append(fitness)

        
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
fn = 'particle50'
o = Rastrigin()

# configuration_settings={'population_size': 100,
#                 'iteration_number': 200,
#                 'weight' : 0.6,
#                 'c1': 0.6,
#                 'c2': 0.2}

# configuration = list(configuration_settings.values())
# b=ParticleSwarmOptimizer(o, configuration, fn, 10)

c1 = [0.5, 1, 1.4]
c2 =  [0.5, 1, 1.4]
w = [2,3,4,5]
x, y = o.best_pos
best = o.evaluate(x, y)

for i in range(5):
    for i in range(len(c1)):
        for j in range(len(c2)):
            if(c1[i] == c2[j]):
                for k in range(len(w)):
                    configuration_settings={'population_size': 120,
                                    'iteration_number': 50,
                                    'weight' : w[k],
                                    'c1': c1[i],
                                    'c2': c2[j],
                                    'optimum globalne': best}

                    configuration = list(configuration_settings.values())
                    b=ParticleSwarmOptimizer(o, configuration, fn)

                    b.initialize_swarm()
                    b.release_the_swarm()
                    b.save_optimal_tracing(configuration_settings)

# b.save_animation('pso')
# b.save_state('pso_hist', False)
# False - historia nie wygląda zbyt ładnie jeszcze