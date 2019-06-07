import abc

class Entity():

    def __init__(self, objective_function):
        self.objective_function = objective_function
        #self.set_entity_initial_parameters()
    

    def set_entity_initial_parameters(self):
        self.x, self.y = self.objective_function.sample_position()
        self.fitness= self.objective_function.evaluate(self.x, self.y)
        self.trial = 0

    # def update_position(self, x, y):
    #     new_fitness= self.evaluate_position(x, y)
        # if(new_fitness >= self.fitness):
        #     self.x = x
        #     self.y = y
        #     self.fitness = new_fitness
        # else:
        #     self.trial += 1

    def evaluate_position(self, x, y):
        return self.objective_function.evaluate(x, y)

    def reset_entity(self):
        self.set_entity_initial_parameters()
        
