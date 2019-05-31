from Optimisation.Optimizer import Optimizer

class ParticleSwarmOptimizer(Optimizer):

     def __init__(self, objective_function, population_size, iteration_number):
        super.__init__(objective_function, population_size, iteration_number)
        
    def initialize_parameters(self):
        super(ParticleSwarmOptimizer, self).initialize_parameters()
        self.initialize_velocities()

    def initialize_velocities(self):
        pass
