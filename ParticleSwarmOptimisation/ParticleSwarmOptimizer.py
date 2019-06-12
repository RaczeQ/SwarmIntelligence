import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
from ObjectiveFunction import ALL_FUNCTIONS, Rosenbrock, Sphere, Trid
from Plotter import Plotter
import logging
import numpy as np
import pandas as pd
import os
class ParticleSwarmOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name, skip_frames=0, plot=True):
        super().__init__(objective_function, configuration[0], configuration[1], result_file_name)
        self.g_best_particle = None
        self.weight = configuration[2]
        self.c1 = configuration[3]
        self.c2 = configuration[4]
        self.skip_frames = skip_frames
        self.plot = plot
        if self.plot:
            self.plotter = Plotter(objective_function, 'PSO')

    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.particles = [Particle(self.objective_function, self.weight, self.c1, self.c2) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for p in self.particles:
            p.save_to_history()
        for i in range(self.iteration_number):
            self.find_g_best()
            self.explore()
            self.update_optimal_solution_tracking()
            if self.plot and (self.skip_frames == 0 or i % self.skip_frames == 0):
                self.plotter.add_frame(i, self.particles)
            # print(i)
            for p in self.particles:
                p.save_to_history()
        if self.plot:
            self.plotter.add_frame(self.iteration_number, self.particles)
            
    def find_g_best(self):
        if self.factor > 0:
            fitness = max(e.p_best_fitness for e in self.particles)
        else:
            fitness = min(e.p_best_fitness for e in self.particles)
        # print('the best fit ===================> '+str(fitness))
        self.g_best_particle = list(filter(lambda b: b.p_best_fitness == fitness, self.particles))
        self.optimal_solution.append(fitness)

        
    def explore(self):
        for i in range(len(self.particles)):
            try:
                self.particles[i].explore_neighborhood(self.g_best_particle)
            except AssertionError:
                pass
                # logging.error("The particle was trying to escape outside the boundaries!")

    def update_optimal_solution_tracking(self):
        if self.factor > 0:
            fitness =  max(e.fitness for e in self.particles) 
        else:
            fitness =  min(e.fitness for e in self.particles)     
        self.optimal_tracing.append(fitness)

    def save_state(self, file_name, line_history):
        assert self.plot
        self.plotter.save_state_to_file(file_name, self.particles, line_history)

#test

# o = Rastrigin()

# configuration_settings={'population_size': 100,
#                 'iteration_number': 200,
#                 'weight' : 0.6,
#                 'c1': 0.6,
#                 'c2': 0.2}

# configuration = list(configuration_settings.values())
# b=ParticleSwarmOptimizer(o, configuration, fn, 10)

c1_list = np.arange(0.2, 2.2, 0.2)
c2_list =  np.arange(0.2, 2.2, 0.2)
w_list = np.arange(0.1, 5.1, 0.1)


for func in [Rosenbrock, Sphere, Trid]:
    fn = f'pso_200_{func.__name__}'
    f = func()
    x, y = f.best_pos
    best = f.evaluate(x, y)
    values = []
    for c1 in c1_list:
        # for c2 in c2_list:
        for c2 in [c1]:
            for w in w_list:
                configuration_settings = {'population_size': 120,
                                        'iteration_number': 50,
                                        'weight' : w,
                                        'c1': c1,
                                        'c2': c2,
                                        'optimum globalne': best,
                                        'function': func.__name__}
                for i in range(10):
                    print(c1, c2, w, i)
                    configuration = list(configuration_settings.values())
                    b=ParticleSwarmOptimizer(f, configuration, fn, plot=False)
                    b.initialize_swarm()
                    b.release_the_swarm()
                    row = b.save_optimal_tracing(configuration_settings)
                    values.append(row)
    df = pd.concat(values, axis=0, ignore_index=True) 
    # file_path = os.path.join('results', f'{fn}.txt')
    df.to_csv(fn)

# b.save_animation('pso')
# b.save_state('pso_hist', False)
# False - historia nie wygląda zbyt ładnie jeszcze