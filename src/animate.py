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

    # nblobs, nfood = headers.count('Blob'), headers.count('Food')
    # print(nblobs, nfood)
    # print(data)

    fig, ax = plt.subplots()
    nblobs, nfood = int(data[0][0]), int(data[0][1])
    x1, y1, fuel = zip(*(data[0][2]))
    x2, y2, value = zip(*(data[0][3]))
    bline, = ax.plot(x1, y1, 'b.')
    fline, = ax.plot(x2, y2, 'y.')
    lines = [bline, fline]
    # lines = []
    # for p1 in range(len(data[0][2])):
    #     print(fuel[p1])
    #     l1, = ax.plot(x1[p1], y1[p1], marker='.', markerfacecolor='blue', markersize=2*fuel[p1]+4, linewidth=0, markeredgewidth=0)
    #     lines.append(l1)
    # for p2 in range(len(data[0][3])):
    #     hue = int(math.ceil(100*(value[p2]-1)))
    #     if hue < 0:
    #         hue = '#'+format(150-abs(hue), 'X')+'FF1b'
    #     else:
    #         hue = '#FF'+format(150-abs(hue), 'X')+'1b'
    #     l2, = ax.plot(x2[p2], y2[p2], markerfacecolor=hue, marker='.', markersize=5, linewidth=0, markeredgewidth=0)
    #     lines.append(l2)

    def animate(i):
        nblobs, nfood = int(data[i][0]), int(data[i][1])
        print('Frame', str(i), ':')
        print(' - ', nblobs, nfood)
        x1, y1, fuel = zip(*(data[i][2]))
        x2, y2, value = zip(*(data[i][3]))
        lines[0].set_data(x1, y1)
        lines[1].set_data(x2, y2)
        return tuple(lines)

        ## NOTE: This code does plot blobs that change color and shape, but it is *incredibly* slow. I need a slicker way of doing this.
        # plt.cla()
        # lines = []
        # for p1 in range(len(data[0][2])):
        #     print(fuel[p1])
        #     l1, = ax.plot(x1[p1], y1[p1], marker='.', markerfacecolor='blue', markersize=2*fuel[p1]+4, linewidth=0, markeredgewidth=0)
        #     lines.append(l1)
        # for p2 in range(len(data[0][3])):
        #     hue = int(math.ceil(100*(value[p2]-1)))
        #     if hue < 0:
        #         hue = '#'+format(150-abs(hue), 'X')+'FF1b'
        #     else:
        #         hue = '#FF'+format(150-abs(hue), 'X')+'1b'
        #     l2, = ax.plot(x2[p2], y2[p2], markerfacecolor=hue, marker='.', markersize=5, linewidth=0, markeredgewidth=0)
        #     lines.append(l2)

    ax.axis([-mapsize, mapsize, -mapsize, mapsize])
    ani = animation.FuncAnimation(fig, animate, frames=len(data) ,interval=50, repeat=False)
    plt.show()
