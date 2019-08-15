#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt
import pickle
import random
import os

from simcontroller import SimController
from animate import ani


# Making Testable code: https://www.toptal.com/qa/how-to-write-testable-code-and-why-it-matters

# random.seed('blob')

def main(nblobs, nfood, maxtime, mapsize):
    '''
    This is the main function of the simulation. Run this to generate simulation data files.
    '''

    if not os.path.exists('../data'):
        print('Created ../data')
        os.makedirs('../data')

    sim = SimController(nblobs, nfood, mapsize)

    filename = '../data/blob_data_'+str(dt.date.today()).replace(' ','_')+'.pickle'
    with open(filename, 'wb') as objf:

        t = 0
        while sim.get_nblobs() > 0 and t < maxtime:
            print('Number of Blobs = ', str(sim.get_nblobs()).rjust(3,'0'), '  Loop = ', t)
            sim.update()
            info = [sim.get_nblobs(), sim.get_nfood()]
            info.append(sim.get_blob_info())
            info.append(sim.get_food_info())
            pickle.dump(list(info), objf)
            t += 1

    return filename

mapsize = 10
f = main(1, 50, 200, mapsize)
ani(f, mapsize)
# ani('blob_data_2019-08-13_big.pickle', 10)
