import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from ObjectiveFunction import Rastrigin, Rosenbrock, Trid, Ackley, Bukin6
from Plotter import Plotter
from Optimisation import Entity

R = Bukin6()
p = Plotter(
    obj_function=R,
    algorithm_name="Random"
)

entities = [
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
]

for i in range(25):
    for e in entities:
        e.set_entity_initial_parameters()

    best_val = entities[2].fitness

    p.add_frame(i, entities, best_val)
    print(i, best_val)

p.save_animation('test')