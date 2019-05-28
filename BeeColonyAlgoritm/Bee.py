

class Bee():

    def __init__(self, objective_function):
        self.objective_function = objective_function
        self.position = objective_function.sample_position()
        self.fitness= objective_function.evaluate_fitness(self.position)
        self.trial = 0 
        self.probability = 0.0

    def update_position(self, new_position, new_fitness):
        if(new_fitness >= self.fitness):
            self.position = new_position
            self.fitness = new_fitness
        else:
            self.trial += 1

       
    def evaluate_position(self, position):
        return 0
       

