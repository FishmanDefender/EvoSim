#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt
import random
import csv
import os

from simcontroller import SimController
from animate import ani

# random.seed('blob')

def main(nblobs, nfood, maxtime, mapsize):
    '''
    This is the main function of the simulation. Run this to generate simulation data files.
    '''

    if not os.path.exists('../data'):
        print('Created ../data')
        os.makedirs('../data')

    sim = SimController(nblobs, nfood, mapsize)

    filename = '../data/blob_data_'+str(dt.date.today()).replace(' ','_')+'.csv'
    with open(filename, 'w') as csvf:

        headers = list(['Blob' for b in range(nblobs)])
        headers.extend(['Food' for f in range(nfood)])

        csvwriter = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        # csvwriter.writerow(headers)

        t = 0
        while sim.get_n_living_blobs() > 0 and t < maxtime:
            print('Number of Blobs = ', sim.get_n_living_blobs(), '  Loop = ', t)
            sim.update()
            info = [sim.get_nblobs(), nfood]
            info.extend(sim.get_blob_info())
            info.extend(sim.get_food_info())
            csvwriter.writerow(list(info))
            t += 1

    return filename

mapsize = 10
f = main(100, 100, 1000, mapsize)
# ani('blob_data_2019-08-12_1.csv', 10)
ani(f, mapsize)
