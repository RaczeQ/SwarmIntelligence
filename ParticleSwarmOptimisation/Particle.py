from Optimisation.Optimizer import Optimizer

class Particle():

    def __init__(self, velocity, objective_function):
        
        self.objective_function = objective_function
        self.position = objective_function.sample_position()
        self.fitness= objective_function.evaluate_fitness(self.position)

        self.velocity = velocity

    def count_new_position(self):
        pass
        