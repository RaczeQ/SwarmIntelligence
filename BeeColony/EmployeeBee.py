from BeeColony.Bee import Bee

class EmployeeBee(Bee):
    
    def __init__(self, max_explore_trials):
        self.max_trials = max_explore_trials

    def explore_neighborhood(self):
        if(self.trial < self.max_trials):
            # wylosuj nową pozycję position
            position = None
            possition_fitness = self.evaluate_position(position)
            self.update_position(position, possition_fitness)

    def get_probability(self):
        # fomula
        return 0