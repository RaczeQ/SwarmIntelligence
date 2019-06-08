import sys
sys.path.insert(1, '.')
from Optimisation.Optimizer import Optimizer
from ParticleSwarmOptimisation.Particle import Particle
from FireflyColonyOptimisation.Firefly import Firefly
from ObjectiveFunction.Rastrigin import Rastrigin

import logging

class FireflyOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name, factor):
        super().__init__(objective_function, configuration[0], configuration[1], result_file_name, factor)
        self.max_beta = configuration[2]
        self.absorption_coefficient = configuration[3]
        self.result_file_name = result_file_name
        self.factor = factor
       
    def initialize_swarm(self):
        self.initialize_particles()

    def initialize_particles(self):
        self.firefly = [Firefly(self.objective_function, self.max_beta, self.absorption_coefficient) for i in range(int(self.population_size))]

    def release_the_swarm(self):
        for k in range(self.iteration_number):
            for i in range(self.population_size):
                for j in range(i):
                    if(i!=j):
                        print("j "+str(j))
                        print(self.firefly[:j])
                        self.firefly[i].explore_neighborhood(self.firefly[:j])
                    else:
                        self.firefly[i].move_firefly()
            self.update_optimal_solution_tracking()

    def update_optimal_solution_tracking(self):
        if(self.factor == 1):
            luminosity =  max(e.luminosity for e in self.firefly) 
        else:
            luminosity =  min(e.luminosity for e in self.firefly) 
        self.optimal_tracing.append(luminosity)        
            
#test
fn = 'firefly'
o = Rastrigin()

configuration_settings={'population_size': 5,
                'iteration_number': 10,
                'max_beta' : 0.7,
                'absorption_coefficient': 0.3}

configuration = list(configuration_settings.values())
b=FireflyOptimizer(o, configuration, fn, -1)

b.initialize_swarm()
b.release_the_swarm()
b.save_optimal_tracing(configuration_settings)
