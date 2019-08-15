#!/usr/bin/env python3
import random
import math

class DNA:
    '''
    Class that holds phenotype information for each blob.
    '''

    def __init__(self, **kwargs):
        '''
        Accepts a dictionary-style input and saves each as an instance variable. This class will have more purpose when Mendelian
        inheritance, sexual reproduction, and phenotypes are implemented.

        Convention dictates that no getter/setter methods are used in python, so I've ommited them from here.
        '''

        ## Core Inherited Parameters ##
        self.hp_max = hp_max
        self.predator = predator

        ## Inherited Modifier Parameters ##
        self.move_speed = move_speed
        self.sprint_speed = sprint_speed
        self.eat_speed = eat_speed
        self.heal_speed = heal_speed
        self.attack_damage = attack_damage
