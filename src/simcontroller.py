#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt
import random
import csv
import sys
import math
import copy

from blob import Blob
from food import Food

class SimController:
    '''
    Controller class for the blobs. This class initiallizes new blobs, controls blob interactions, and updates blob positions. This also
    manages food on the pertri dish surface.
    '''

    def __init__(self, nblobs, nfood, mapsize):
        '''
        Initializes the SimController class and all initial blobs.
        '''

        self.mapsize = mapsize

        self.dead_blobs_index = []
        self.blobs = {}
        self.food  = {}

        for n in range(nblobs):
            self.add_blob(n)

        for m in range(nfood):
            self.add_food(m)

    def update(self):
        '''
        Moves all of the blobs 1 timestep
        '''

        for bkey in list(self.blobs.keys()):

            blob = self.blobs[bkey]
            xb, yb = blob.get_x(), blob.get_y()

            min_r = sys.float_info.max
            mindex = 0
            minth  = 2*math.pi*random.random()
            for fkey in list(self.food.keys()):
                food = self.food[fkey]
                xf, yf = food.get_x(), food.get_y()
                r = math.sqrt((xb - xf)**2 + (yb - yf)**2)
                theta = np.arctan2((yf - yb), (xf - xb))
                if r < min_r:
                    min_r = r
                    mindex = fkey
                    minth = theta

            if not blob.move(min_r, minth):
                if not bkey in self.dead_blobs_index:
                    print('Blob ', str(blob.get_id()).rjust(4,'0'), ' Starved')
                    self.dead_blobs_index.append(bkey)
                    del self.blobs[bkey]
                    continue

            food = self.food[mindex]
            xb, yb = blob.get_x(), blob.get_y()
            xf, yf = food.get_x(), food.get_y()
            r = math.sqrt((xb - xf)**2 + (yb - yf)**2)
            if r < 0.1:
                blob.eat(food.get_food_value())
                del self.food[mindex]
                self.add_food(mindex)

            self.blobs_multi()

    def blobs_multi(self):

        use_fuel = 1.5
        pause = 4
        for bkey in list(self.blobs.keys()):

            blob = self.blobs[bkey]
            if blob.get_fuel() > 2:
                if not self.dead_blobs_index:
                    id = self.get_nblobs()+1
                    self.blobs[id] = Blob(id, self.mapsize, blob.get_x(), blob.get_y(), wait=pause)
                    blob.use_fuel(use_fuel)
                else:
                    id = self.dead_blobs_index.pop(0)
                    self.blobs[id] = Blob(id, self.mapsize, blob.get_x(), blob.get_y(), wait=pause)
                    blob.use_fuel(use_fuel)

    def get_blob_info(self):
        '''
        Returns current location of all blobs.
        '''

        blob_info = [(self.blobs[key].get_x(), self.blobs[key].get_y(), self.blobs[key].get_fuel()) for key in list(self.blobs.keys())]
        return blob_info

    def get_food_info(self):
        '''
        Returns current location of all food.
        '''

        food_info = [(self.food[key].get_x(), self.food[key].get_y(), self.food[key].get_food_value()) for key in list(self.food.keys())]
        return food_info

    def add_blob(self, id):

        self.blobs[id] = Blob(id, self.mapsize)

    def add_food(self, id):

        self.food[id] = Food(id, self.mapsize)

    def get_nblobs(self):

        return len(self.blobs)

    def get_nfood(self):

        return len(self.food)

    def get_n_living_blobs(self):

        return len(self.blobs) - len(self.dead_blobs_index)
