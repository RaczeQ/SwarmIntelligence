import abc

class Entity():

    def __init__(self, objective_function):
        self.objective_function = objective_function
        self.position = objective_function.sample_position()
        self.position_value= objective_function.evaluate_position(self.position)
        self.trial = 0

    def update_position(self, new_position):
        new_position_value= self.evaluate_position(new_position)
        if(new_position_value >= self.position_value):
            self.position = new_position
            self.position_value = new_position_value
        else:
            self.trial += 1

    def evaluate_position(self, position):
        return self.objective_function.evaluate_position(position)

    def reset_entity(self):
        self.trial = 0


        
    @abc.abstractmethod
    def count_new_position(self):   
        return