import numpy as np

class ObjectiveFunction():

    def __init__(self, dimention):

        self.dimention = dimention #array ?
        self.x_min = 0 # ?
        self.x_max = 0 # ?
        self.sources=[]

    def count_objective_function(self):
        pass


    def evaluate_position(self, position):
        pass
    
    #zwraca losowe indeksy nowej pozycji
    def sample_position(self):
        pass


