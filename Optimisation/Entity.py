class Entity(object):
    x = None
    y = None
    fitness = None
    color = None
    history_of_points = []

    def __init__(self, objective_function, factor = 1):
        self.objective_function = objective_function
        self.factor = factor

    def set_entity_initial_parameters(self):
        self.x, self.y = self.objective_function.sample_position()
        self.fitness= self.objective_function.evaluate(self.x, self.y)
        self.trial = 0
       # print("initial x="+str(self.x) + " initial y="+str(self.y) + ' initial fitness='+str(self.fitness))

    def set_new_position(self, x, y):
        self.history_of_points.append((self.x, self.y))
        self.x = x
        self.y = y

    def evaluate_position(self, x, y):
        return self.objective_function.evaluate(x, y)

    def reset_entity(self):
        self.set_entity_initial_parameters()
        

