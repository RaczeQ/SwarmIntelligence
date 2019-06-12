import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from FireflyColonyOptimisation.Firefly import Firefly
from ObjectiveFunction.Rastrigin import Rastrigin
from Plotter import Plotter

import logging

class FireflyOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name, skip_frames=0, plot=True):
        super().__init__(objective_function, configuration[0], configuration[1], result_file_name)
        self.max_beta = configuration[2]
        self.absorption_coefficient = configuration[3]
        self.result_file_name = result_file_name
        self.factor = objective_function.factor
        self.skip_frames = skip_frames
        self.plot = plot
        if self.plot:
            self.plotter = Plotter(objective_function, 'Firefly')
       
    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.fireflies = [Firefly(self.objective_function, self.max_beta, self.absorption_coefficient) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for f in self.fireflies:
            f.save_to_history()
        for k in range(self.iteration_number):
            for i in range(self.population_size):
                for j in range(i):
                    if(i!=j):
                        self.fireflies[i].explore_neighborhood(self.fireflies[:j])
                    else:
                        self.fireflies[i].move_fireflies()
            if self.plot and (self.skip_frames == 0 or i % self.skip_frames == 0):
                self.plotter.add_frame(k, self.fireflies)
            # print(k)
            self.update_optimal_solution_tracking()
            for f in self.fireflies:
                f.save_to_history()
        if self.plot:
            self.plotter.add_frame(self.iteration_number, self.fireflies)

    def update_optimal_solution_tracking(self):
        if(self.factor == 1):
            luminosity =  max(e.luminosity for e in self.fireflies) 
        else:
            luminosity =  min(e.luminosity for e in self.fireflies) 
        self.optimal_tracing.append(luminosity)   
        self.optimal_solution.append(luminosity)     
        print('the best luminosity ===================> '+ str(luminosity))       
    
    def save_state(self, file_name, line_history):
        assert self.plot
        self.plotter.save_state_to_file(file_name, self.fireflies, line_history)
            
# #test
# fn = 'fireflies'
# o = Rastrigin()

# configuration_settings={'population_size': 20,
#                 'iteration_number': 100,
#                 'max_beta' : 0.7,
#                 'absorption_coefficient': 0.3}

# configuration = list(configuration_settings.values())
# b=FireflyOptimizer(o, configuration, fn, 5)

# b.initialize_swarm()
# b.release_the_swarm()
# b.save_optimal_tracing(configuration_settings)
# b.save_animation('fireflies')
# b.save_state('fireflies_hist', False)
            
#test
fn = 'firefly50'
o = Rastrigin()

max_beta=[0.2, 0.3]
absorption_coefficient = [0.2, 0.3]

for i in range(len(max_beta)):
    for j in range(len(absorption_coefficient)):
        configuration_settings={'population_size': 50,
                        'iteration_number': 50,
                        'max_beta' : 0.7,
                        'absorption_coefficient': 0.3}
        configuration = list(configuration_settings.values())
        b=FireflyOptimizer(o, configuration, fn)

        b.initialize_swarm()
        b.release_the_swarm()
        b.save_optimal_tracing(configuration_settings)
