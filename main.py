import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from ObjectiveFunction import Rastrigin, Rosenbrock, Trid, Ackley, Bukin6, Sphere
from Plotter import Plotter
from Optimisation import Entity

R = Sphere()
p = Plotter(
    obj_function=R,
    algorithm_name="Sphere"
)

entities = [
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
    Entity(R),
]

# for i in range(1):
#     for e in entities:
#         e.set_entity_initial_parameters()

#     p.add_frame(i, entities)
#     print(i)

# p.save_animation('test')

p.save_state_to_file('sphere', [])