#!/usr/bin/env python3
import random
import math

class DNA:
    '''
    Class that holds phenotype information for each blob.
    '''

    def __init__(self, hp_max, predator, mutation_rate, move_speed, sprint_param, eat_param, heal_param, attack_damage, craving, **kwargs):
        '''
        Accepts a dictionary-style input and saves each as an instance variable. This class will have more purpose when Mendelian
        inheritance, sexual reproduction, and phenotypes are implemented.

        Convention dictates that no getter/setter methods are used in python, so I've ommited them from here.
        '''

        ## Core Inherited Parameters ##
        self.hp_max = hp_max
        self.predator = predator
        self.mutation_rate = mutation_rate

        ## Inherited Modifier Parameters ##
        self.move_speed = move_speed
        self.sprint_param = sprint_param
        self.eat_param = eat_param
        self.heal_param = heal_param
        self.attack_damage = attack_damage
        self.craving = craving

    def mutate(self):
        '''
        Modifies all instance variables by a small amount determined by self.mutation_rate
        '''

        self.hp_max += (2*random.random() - 1)*mutation_rate
        self.predator += (2*random.random() - 1)*mutation_rate
        self.mutation_rate += (0.2*random.random() - 1)*mutation_rate

        self.move_speed += (2*random.random() - 1)*mutation_rate
        self.sprint_param += (2*random.random() - 1)*mutation_rate
        self.eat_param += (2*random.random() - 1)*mutation_rate
        self.heal_param += (2*random.random() - 1)*mutation_rate
        self.attack_damage += (2*random.random() - 1)*mutation_rate
        self.craving += (2*random.random() - 1)*mutation_rate

        # TODO: Try turning the following off to see if it makes a difference. Death should cull any values < 0.

        if self.hp_max < 0:
            self.hp_max = 0
        if self.predator < 0:
            self.predator = 0
        elif self.predator > 1:
            self.predator = 1
        if self.mutation_rate < 0.01:
            self.mutation_rate = 0.01
        if self.move_speed < 0:
            self.move_speed = 0
        if self.sprint_param < 0:
            self.sprint_param = 0
        if self.eat_param < 0:
            self.eat_param = 0
        if self.heal_param < 0:
            self.heal_param = 0
        if self.attack_damage < 0:
            self.attack_damage = 0
        if self.craving < 0:
            self.craving = 0
