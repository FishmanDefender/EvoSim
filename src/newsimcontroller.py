#!/usr/bin/env python3
import math
import random
import numpy as np
import configparser
import sys

from blob import Blob
from food import Food
from dna import DNA

class SimController:
    '''
    Last Update: DNA Update
    Version: Pre-Alpha 0.0.1

    Controller class for the simulation. This class manages all blob and food objects, updates their positions, manages blob interactions,
    and creates new blob and food objects as needed.
    '''

    def __init__(self, nblobs, nfood, mapsize):

        self.mapsize = mapsize

        self.blobs, self.food = {}, {}

        for i in range(nblobs):
            x, y = ((2*random.random())-1)*self.mapsize), ((2*random.random())-1)*self.mapsize)
            self.new_blob(i, self.default_dna(), x, y)

        for j in range(nfood):
            x, y = ((2*random.random())-1)*self.mapsize), ((2*random.random())-1)*self.mapsize)
            self.new_food(j, x, y)

        self.dead_blobs_index = []

    ## External Functions ##

    def Update(self):
        '''
        Update calls an action function in each blob based on the blob's state. This method will at some point be replaced by
        a dedicated blob AI class that will make these decisions *inside* each blob.
        '''

        for i in range(len(self.blobs)):

            blob = self.blobs[i]
            blob.check_dead()

            if blob.is_dead:
                if blob.food <= 0:
                    del self.blobs[i]
                    self.dead_blobs_index.append(i)
                    continue
                else:
                    blob.get_eaten(1)
                continue

            blob.reset_already_acted()
            bx, by = blob.x, blob.y

            if blob.hp < blob.max_hp and self.fuel > blob.craving:

                blob.heal()

            else:

                reach = 0.1 # TODO: Maybe make this based on blob.hp_max
                minr, minth, minid = sys.float.max, 0, -1
                if blob.predator:
                    for j in range(len(self.blobs)):
                        food = self.blobs[j]
                        fx, fy = food.x, food.y
                        r, th = math.sqrt((xb - xf)**2 + (yb - yf)**2), np.arctan2((yf - yb), (xf - xb))
                        if r < minr:
                            minr, minth, minid = r, th, j
                    if minr < reach:
                        target = self.blobs[minid]
                        if target.is_dead:
                            blob.eat_corpse(target)
                        else:
                            blob.attack(target)

                elif blob.target:
                    blob.sprint(blob.hunter_theta)

                else:
                    for j in range(len(self.food)):
                        food = self.food[j]
                        fx, fy = food.x, food.y
                        r, th = math.sqrt((xb - xf)**2 + (yb - yf)**2), np.arctan2((yf - yb), (xf - xb))
                        if r < minr:
                            minr, minth, minid = r, th, j
                    if minr < reach:
                        blob.eat(self.food[minid])
                    else:
                        blob.move(minth)


    def get_nblobs(self):
        '''
        Returns the number of blobs in the blob dictionary
        '''

        return len(self.blobs)

    ## Internal Functions ##

    def add_blob(self, id, dna, xpos, ypos):
        '''
        Creates a blob creature and adds it to the blob dictionary
        '''

        self.blobs[id] = Blob(id, dna, xpos, ypos)

    def add_food(self, id, xpos, ypos):
        '''
        Creates a food object and adds it to the food dictionary
        '''

        self.food[id] = Blob(id, dna, xpos, ypos)


    def default_dna(self):
        '''
        Reads in the information from config/default_dna.config using ConfigParser. Returns a DNA object.
        '''

        config = configparser.ConfigParser()
        config.read('../config/default_dna.config')
        conf_in = dict(config.items('DEFAULT'))

        def_dna = DNA(**conf_in)

        return def_dna
