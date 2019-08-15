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

    def __init__(self, dna, xpos, ypos, init_fuel = 10, exponent = 1.2, last_attack = 10):
        '''
        Creates a new blob creature using the passed DNA object at the location xpos and ypos.
        '''

        ## Passed Values ##
        self.dna = dna
        self.fuel = init_fuel
        self.x = xpos
        self.y = ypos

        self.exponent = exponent

        ## Inherited Parameters ##
        self.max_hp = self.dna.max_hp
        self.move_speed = self.dna.move_speed
        self.sprint_param = self.dna.sprint_param
        self.eat_param = self.dna.eat_param
        self.heal_param = self.dna.heal_param
        self.attack_damage = self.dna.attack_damage

        ## Derived Parameters ##
        self.hp = self.max_hp
        self.base_fuel_cost = 0.1*self.max_hp
        self.predator = self.dna.get_predator()
        self.food = (self.fuel**2)*self.max_hp

        ## Detected Parameters ##
        self.closest_food_theta = 0
        self.hunter_theta = 0
        self.hunter_r = 0

        ## State Parameters ##
        self.is_target = False
        self.is_hunter = False
        self.already_acted = False

        ## Counting Parameters ##
        self.last_attack = last_attack

    ## Action Methods ##

    def move(self, angle):
        '''
        Moves the blob in the direction determined by angle and subtracts the fuel cost from self.fuel. Checking bounds is now done in
        the sim controller. self.exponent should be greater than 1 so the fuel cost increases nonlinearly.
        '''

        self.x += self.move_speed*math.cos(angle)
        self.y += self.move_speed*math.sin(angle)
        self.fuel -= self.base_fuel_cost*(self.move_speed*self.fuel)**self.exponent
        self.already_acted = True

    def sprint(self, angle):

        self.x += self.sprint_param*self.move_speed*math.cos(angle)
        self.y += self.sprint_param*self.move_speed*math.sin(angle)
        self.fuel -= self.base_fuel_cost*(self.sprint_param*self.move_speed*self.fuel)**self.exponent
        self.already_acted = True

    def eat(self, food_obj):
        '''
        Increases the fuel reserves of the blob at the rate determined by self.eat_param and removes the value of the food object by the same
        amount
        '''

        value = self.eat_param - 0.1*(self.eat_param**self.exponent)*self.base_fuel_cost
        self.fuel += value
        food_obj.value -= value
        self.already_acted = True

    def heal(self):
        '''
        Increases the health of the blobs after experiencing some damage. The rate is determined by self.heal_param.
        '''

        self.hp += self.heal_param
        self.fuel -= 0.1*(self.heal_param**self.exponent)*self.base_fuel_cost
        self.already_acted = True

    def attack(self, target):
        '''
        Decreases the health of the target and passes current location to the target.
        '''

        target.take_damage(self.attack_damage, self.x, self.y)
        self.fuel -= (self.attack_damage**self.exponent)*self.base_fuel_cost
        self.already_acted = True


    ## Non-Action Methods ##

    def take_damage(self, damage, hunter_x, hunter_y):
        '''
        Recieves the damage from a hunter and records the hunter's x and y coordinates.
        '''

        if not self.target: self.target = True
        self.hp -= damage
        self.hunter_r = math.sqrt((hunter_x - self.x)**2 + (hunter_y - self.y)**2)
        self.hunter_theta = np.arctan2((hunter_y - self.y), (hunter_x - self.x))
        self.last_attack = 0

    def reset_already_acted(self):
        '''
        Resets action counter so the blob will move next time step.
        '''

        self.already_acted = False

    def increase_safty(self):
        '''
        If the blob wasn't attacked this turn and it is a target, then self.last_attack increases by 1.
        '''

        if self.is_target:
            if self.last_attack != 0:
                self.last_attack += 1
            elif self.last_attack < 0:
                raise ValueError('last_attack somehow decreased')
            elif self.last_attack > 10:
                self.last_attack = 0
                self.is_target = False
            else:
                raise ValueError('last_attack is not a number')
