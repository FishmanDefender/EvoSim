import configparser

class Test:

    def __init__(self, hp_max, predator, move_speed, sprint_param, eat_param, heal_param, attack_damage, **kwargs):

        ## Core Inherited Parameters ##
        self.hp_max = hp_max
        self.predator = predator

        ## Inherited Modifier Parameters ##
        self.move_speed = move_speed
        self.sprint_param = sprint_param
        self.eat_param = eat_param
        self.heal_param = heal_param
        self.attack_damage = attack_damage

    def run_test(self):

        ## Core Inherited Parameters ##
        print(self.hp_max)
        print(self.predator)

        ## Inherited Modifier Parameters ##
        print(self.move_speed)
        print(self.sprint_param)
        print(self.eat_param)
        print(self.heal_param)
        print(self.attack_damage)

config = configparser.ConfigParser()
config.read('default_dna.config')

conf_in = dict(config.items('DEFAULT'))
print(conf_in)

test = Test(**conf_in)
test.run_test()
