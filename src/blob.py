#!/usr/bin/env python3
import random
import math


class Blob:
    '''
    Creates a blob creature. Blob creatures are "born" with a full hunger bar and a random starting location.
    The move speed determines how many spaces they can travel per time step. Their hunger depletes at 0.1 per time step.
    '''

    ##### CONSTRUCTOR #####

    def __init__(self, id, mapsize, x=None, y=None):

        if x == None:
            self.x = ((2*random.random())-1)*mapsize
        else:
            self.x = x

        if y == None:
            self.y = ((2*random.random())-1)*mapsize
        else:
            self.y = y

        self.id = id
        self.mapsize = mapsize
        self.wait = 0

        self.move_speed = 0.1
        self.fuel = 1
        self.hunger_modifier = 0.02

    ##### PUBLIC METHODS #####

    def test_pos(self):

        print('ID: ', self.id, ' -- X: ', self.x, ' -- Y: ', self.y)

    def move(self, closest_food_r, closest_food_theta):

        if not self.__isdead():

            if self.wait > 0:

                self.wait -= 1

            else:

                self.wait = 0
                direction = closest_food_theta #2*math.pi*random.random()

                self.x += math.cos(direction)*self.move_speed
                self.y += math.sin(direction)*self.move_speed

                self.__fix_bounds()
                self.use_fuel(self.hunger_modifier)

            return True

        else:

            self.x = -(self.mapsize + 1)
            self.y = -(self.mapsize + 1)

            return False

    def eat(self, food_modifier):

        self.fuel += 1*food_modifier

    def use_fuel(self, hunger_modifier):

        self.fuel -= 1*hunger_modifier

    def set_wait(self, wait):

        self.wait = wait

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y

    def get_id(self):

        return self.id

    def get_fuel(self):

        return self.fuel

    ##### PRIVATE METHODS #####

    def __isdead(self):
        '''
        Checks if the blob has starved.
        '''

        if self.fuel <= 0:
            self.fuel = 0
            return True

        else:
            return False

    def __fix_bounds(self):
        '''
        Keeps the blob inside the petri dish. The blob is simply moved back onto the dish in a stright line if it were to escape.
        '''

        if self.x > self.mapsize:
            self.x = self.mapsize
        elif self.x < -self.mapsize:
            self.x = -self.mapsize

        if self.y > self.mapsize:
            self.y = self.mapsize
        elif self.y < -self.mapsize:
            self.y = -self.mapsize
