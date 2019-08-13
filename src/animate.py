#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import datetime as dt
import math
import random
import csv

def ani(filename, mapsize):
    '''
    This is the visualization function. Run this to plot a 2D histogram with points corresponding to blobs.
    '''

    # BUG: The current CSV writing system starts pushing the food to later columns as more blobs are created.
    #       THIS IS STILL BROKEN!!


    data = []
    nvals = []
    with open('../data/'+filename) as csvf:
        csvreader = csv.reader(csvf, delimiter=',')
        # headers = next(csvreader)
        for line in csvreader:
            nvals.append(line[0:2])
            tups = []
            for tup in line[2:]:
                x, y, z = [float(val) for val in tup.strip('()').split(',')]
                tups.append((x,y,z))
            data.append(tups)

    # nblobs, nfood = headers.count('Blob'), headers.count('Food')
    # print(nblobs, nfood)
    # print(data)

    fig, ax = plt.subplots()
    nblobs, nfood = int(nvals[0][0]), int(nvals[0][1])
    x1, y1, fuel = zip(*(data[0][0:nblobs]))
    x2, y2, value = zip(*(data[0][nblobs:]))
    bline, = ax.plot(x1, y1, 'b.')
    fline, = ax.plot(x2, y2, 'y.')
    lines = [bline, fline]
    # lines = []
    # for p1 in range(len(x1)):
    #     print(fuel[p1])
    #     l1, = ax.plot(x1[p1], y1[p1], marker='.', markerfacecolor='blue', markersize=2*fuel[p1]+4, linewidth=0, markeredgewidth=0)
    #     lines.append(l1)
    # for p2 in range(len(x2)):
    #     hue = int(math.ceil(100*(value[p2]-1)))
    #     if hue < 0:
    #         hue = '#'+format(150-abs(hue), 'X')+'FF1b'
    #     else:
    #         hue = '#FF'+format(150-abs(hue), 'X')+'1b'
    #     l2, = ax.plot(x2[p2], y2[p2], markerfacecolor=hue, marker='.', markersize=5, linewidth=0, markeredgewidth=0)
    #     line.append(l2)

    def animate(i):
        nblobs, nfood = int(nvals[i][0]), int(nvals[i][1])
        print(nblobs, nfood)
        print('         Frame', str(i), end='\r')
        x1, y1, fuel = zip(*(data[i][0:nblobs]))
        x2, y2, value = zip(*(data[i][nblobs:]))
        lines[0].set_data(x1, y1)
        lines[1].set_data(x2, y2)
        # for j, line in enumerate(lines[0:nblobs]):
        #     line.set_data(x1[j], y1[j])
        #     line.set_markersize(2*fuel[j]+4)
        # for k, line in enumerate(lines[nblobs:]):
        #     line.set_data(0, 0)
        #     line.set_data(x2[k], y2[k])
        #     hue = int(math.ceil(1e3*(value[k]-1)))
        #     if hue < 0:
        #         hue = '#'+format(150-abs(hue), 'X')+'FF1b'
        #     else:
        #         hue = '#FF'+format(150-abs(hue), 'X')+'1b'
        #     line.set_markerfacecolor(hue)
        # return tuple(lines)
        return bline, fline,

    ax.axis([-mapsize, mapsize, -mapsize, mapsize])
    ani = animation.FuncAnimation(fig, animate, interval=50)
    plt.show()
