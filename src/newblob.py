#!/usr/bin/env python3
import random
import math

class Blob:
    '''
    Last Update: DNA Update Blob
    Version: Pre-Alpha 0.0.1

    Blobs contain variables to define a creature state. Each blob creature has a DNA object that contains inherited parameter values,
    has a method for each blob action, and has instance variables that reflect the current state of the blob.
    '''

    def __init__(self, dna, xpos, ypos, init_fuel=10):
        '''
        Creates a new blob creature using the passed DNA object at the location xpos and ypos.
        '''

        ## Passed Values ##
        self.dna = dna
        self.fuel = init_fuel
        self.x = xpos
        self.y = ypos

        ## Inherited Parameters ##
        self.max_hp = self.dna.max_hp
        self.move_speed = self.dna.move_speed
        self.sprint_speed = self.dna.sprint_speed
        self.eat_speed = self.dna.eat_speed
        self.heal_speed = self.dna.heal_speed
        self.attack_damage = self.dna.attack_damage

        ## Derived Parameters ##
        self.hp = self.max_hp
        self.base_fuel_cost = 0.1*self.max_hp
        self.predator = self.dna.get_predator()
        self.food = (self.fuel**2)*self.max_hp
