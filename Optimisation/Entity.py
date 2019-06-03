import abc

class Entity():

    def __init__(self, objective_function):
        self.objective_function = objective_function
        self.set_entity_initial_parameters()
    

    def set_entity_initial_parameters(self):
        self.x, self.y = self.objective_function.sample_position()
        self.position_value= self.objective_function.evaluate(self.x, self.y)
        self.trial = 0

    def update_position(self, x, y):
        new_position_value= self.evaluate_position(x, y)
        if(new_position_value >= self.position_value):
            self.x = x
            self.y = y
            self.position_value = new_position_value
        else:
            self.trial += 1

    def evaluate_position(self, x, y):
        return self.objective_function.evaluate(x, y)

    def reset_entity(self):
        self.set_entity_initial_parameters()
        


    @abc.abstractmethod
    def count_new_position(self):   
        return