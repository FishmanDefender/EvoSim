#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt
import math
import random
import pickle

def ani(filename, mapsize):
    '''
    This is the visualization function. Run this to plot a 2D histogram with points corresponding to blobs.
    '''

    # TODO: Add support for visulization differences in each blob/food.

    data = []
    with open('../data/'+filename, 'rb') as objf:
        while True:
            try:
                data.append(pickle.load(objf))
            except EOFError:
                break

    fig, ax = plt.subplots()
    nblobs, nfood = int(data[0][0]), int(data[0][1])
    x1, y1, fuel = zip(*(data[0][2]))
    x2, y2, value = zip(*(data[0][3]))
    bline, = ax.plot(x1, y1, 'b.')
    fline, = ax.plot(x2, y2, 'y.')
    lines = [bline, fline]

    def animate(i):
        nblobs, nfood = int(data[i][0]), int(data[i][1])
        print('Frame', str(i), ':')
        print(' - ', nblobs, nfood)
        x1, y1, fuel = zip(*(data[i][2]))
        x2, y2, value = zip(*(data[i][3]))
        lines[0].set_data(x1, y1)
        lines[1].set_data(x2, y2)
        return tuple(lines)

    ax.axis([-mapsize, mapsize, -mapsize, mapsize])
    ani = animation.FuncAnimation(fig, animate, frames=len(data) ,interval=50, repeat=False)
    plt.show()
    # plt.plot([int(nblobs[0]) for nblobs in data])
    # plt.show()
