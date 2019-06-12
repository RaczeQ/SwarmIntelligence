import sys
sys.path.insert(1, '.')

from Optimisation.Optimizer import Optimizer
from EmployeeBee import EmployeeBee
from OnLookerBee import OnLookerBee
from ObjectiveFunction import Ackley, Rastrigin, Bukin6, Rosenbrock, Trid
import numpy as np
import logging
from Plotter import Plotter


class BeeOptimizer(Optimizer):

    def __init__(self, objective_function, configuration, result_file_name, skip_frames=0, plot=True):
        super().__init__(objective_function, configuration[0], configuration[1] ,result_file_name)
        self.max_trials = configuration[2]
        self.skip_frames = skip_frames
        self.plot = plot
        if self.plot:
            self.plotter = Plotter(objective_function, 'Bees')

    def initialize_swarm(self):
        self.initialize_population()

    def initialize_population(self):
        self.initialize_employees()
        self.initialize_outlookers()

    def initialize_employees(self):
        self.employeed = [EmployeeBee(self.objective_function, self.max_trials)  for i in range(int(self.population_size/2))]

    def initialize_outlookers(self):
        self.outlookers = [OnLookerBee(self.objective_function) for  i in range(int(self.population_size/2))]

    def release_the_swarm(self):
        for b in self.employeed + self.outlookers:
            b.save_to_history()
        for i in range(self.iteration_number):
            self.explore()
            self.calculate_probabilities()
            self.find_best_bees()
            self.onlook()
            self.update_optimal_solution_tracking()
<<<<<<< HEAD
            #self.plotter.add_frame(i, self.employeed + self.outlookers)
            print(i)
=======
            if self.plot and (self.skip_frames == 0 or i % self.skip_frames == 0):
                self.plotter.add_frame(i, self.employeed + self.outlookers)
            # print(i)
            for b in self.employeed + self.outlookers:
                b.save_to_history()
        if self.plot:
            self.plotter.add_frame(self.iteration_number, self.employeed + self.outlookers)
>>>>>>> 74c760c2310adfa0e78a35b37f94f85b43b2e57a
            
    def explore(self):
        self.make_employee_bees_working()

    def calculate_probabilities(self):
        sum_fitness = sum(x.fitness for x in self.employeed)
        for i in range(len(self.employeed)):
            self.employeed[i].count_probability(sum_fitness)

    def find_best_bees(self):
        if(self.factor == 1):
            prob = max(e.probability for e in self.employeed)
        else:
            prob = min(e.probability for e in self.employeed)
        best_bee = list(filter(lambda b: b.probability == prob, self.employeed))
        self.best_bees = best_bee

    def onlook(self):
        self.make_onlooker_bees_working()

    def update_optimal_solution_tracking(self):
        if(self.factor == 1):
            outlooker_fitness =  max(e.fitness for e in self.outlookers) 
            employee_fitness = max(e.fitness for e in self.employeed) 
        else:
            outlooker_fitness =  min(e.fitness for e in self.outlookers) 
            employee_fitness =  min(e.fitness for e in self.employeed) 
        self.optimal_tracing.append(outlooker_fitness)
        self.optimal_solution.append(employee_fitness)

    def make_employee_bees_working(self):
        neighborhood = self.get_neighborhood_positions()
        for i in range(len(self.employeed)):
            copy = neighborhood.copy()
            copy.pop(i)
            self.employeed[i].explore_neighborhood(copy)
        
    def get_neighborhood_positions(self):
        return [ [self.employeed[i].x, self.employeed[i].y] for i in range(len(self.employeed)) ]

    def make_onlooker_bees_working(self):
        for i in range(len(self.outlookers)):
            self.outlookers[i].onlook(self.best_bees, self.max_trials)

    def save_state(self, file_name, line_history):
        assert self.plot
        self.plotter.save_state_to_file(file_name, self.employeed + self.outlookers, line_history)

#test
<<<<<<< HEAD
fn = 'bee50_3'
=======

# fn = 'bee'
# o = Rosenbrock()

# configuration_settings={'population_size': 100,
#                 'iteration_number': 300,
#                 'max_trials' : 5}

# configuration = list(configuration_settings.values())
# b=BeeOptimizer(o, configuration, fn, 10)

fn = 'bee50_2'
>>>>>>> 74c760c2310adfa0e78a35b37f94f85b43b2e57a
o = Rastrigin()
x, y = o.best_pos
best = o.evaluate(x, y)
#5, 10, 15,
population_size = [10, 30, 50, 70, 100]
trials_num = [10,20,30] #[5,7,10,12,15,17,20,22,25,27,30]


<<<<<<< HEAD
for l in range(10):
    for i in range(len(population_size)):
            for k in range(len(trials_num)):
                configuration_settings={'rozmiar populacji': population_size[i],
                                'liczba iteracji': 50,
                                'liczba prób' : trials_num[k],
                                'optimum globalne': best}

                configuration = list(configuration_settings.values())
                b=BeeOptimizer(o, configuration, fn)
=======
# for i in range(len(population_size)):
#         for k in range(len(trials_num)):
#             configuration_settings={'rozmiar populacji': population_size[i],
#                             'liczba iteracji': 50,
#                             'liczba prób' : trials_num[k],
#                             'optimum globalne': best}

#             configuration = list(configuration_settings.values())
#             b=BeeOptimizer(o, configuration, fn)
>>>>>>> 74c760c2310adfa0e78a35b37f94f85b43b2e57a

                b.initialize_swarm()
                b.release_the_swarm()
                b.save_optimal_tracing(configuration_settings)

#b.save_animation('bees')
#b.save_state('bees_hist', False)
# False - historia nie wygląda zbyt ładnie jeszcze


# fn = 'bee50_goal'
# goal = [Rastrigin(), Ackley(), Bukin6(), Rosenbrock(), Trid]
# for i in range(len(goal)):
#     o= goal[i]
#     x, y = o.best_pos
#     best = o.evaluate(x, y)
#     configuration_settings={'rozmiar populacji': 30,
#                             'liczba iteracji': 50,
#                             'liczba prób' : 30,
#                             'optimum globalne': best,
#                             'funkcja oceny': o.__class__.__name__}

#     configuration = list(configuration_settings.values())
#     b=BeeOptimizer(o, configuration, fn)

#     b.initialize_swarm()
#     b.release_the_swarm()
#     b.save_optimal_tracing(configuration_settings)

