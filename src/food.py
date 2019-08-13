#!/usr/bin/env python3
import random
import math

class Food:
    '''
    Creates a food object.
    '''

    def __init__(self, id, mapsize):
        '''
        Creates a food object
        '''

        self.id = id
        self.mapsize = mapsize
        self.food_value = 1 + (0.2*random.random() - 0.1)

        self.x = ((2*random.random())-1)*self.mapsize
        self.y = ((2*random.random())-1)*self.mapsize

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y

    def get_id(self):

        return self.id

    def get_food_value(self):

        return self.food_value
