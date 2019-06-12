import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from FireflyColonyOptimisation.Firefly import Firefly
from ObjectiveFunction.Rastrigin import Rastrigin

import logging

class FireflyOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name):
        super().__init__(objective_function, configuration[0], configuration[1], result_file_name)
        self.max_beta = configuration[2]
        self.absorption_coefficient = configuration[3]
        self.result_file_name = result_file_name
       
    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.firefly = [Firefly(self.objective_function, self.max_beta, self.absorption_coefficient) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for k in range(self.iteration_number):
            for i in range(self.population_size):
                for j in range(i):
                    if(i!=j):
                        self.firefly[i].explore_neighborhood(self.firefly[:j])
                    else:
                        self.firefly[i].move_firefly()
            self.update_optimal_solution_tracking()

    def update_optimal_solution_tracking(self):
        if(self.factor> 0 ):
            luminosity =  max(e.luminosity for e in self.firefly) 
        else:
            luminosity =  min(e.luminosity for e in self.firefly) 
        self.optimal_tracing.append(luminosity)   
        self.optimal_solution.append(luminosity)     
        print('the best luminosity ===================> '+ str(luminosity))
            
#test
fn = 'firefly50'
o = Rastrigin()

max_beta=[0.2, 0.3]
absorption_coefficient = [0.2, 0.3]
x, y = o.best_pos
best = o.evaluate(x, y)

for i in range(len(max_beta)):
    for j in range(len(absorption_coefficient)):
        configuration_settings={'population_size': 50,
                        'iteration_number': 50,
                        'max_beta' : max_beta[i],
                        'absorption_coefficient': absorption_coefficient[j],
                        'optimum globalne': best}

        configuration = list(configuration_settings.values())
        b=FireflyOptimizer(o, configuration, fn)

        b.initialize_swarm()
        b.release_the_swarm()
        b.save_optimal_tracing(configuration_settings)
