import random
import os
class Tank:
    def __init__(self, name, armor, ammo):
        self.tank_name = name
        self.armor = armor
        self.ammo = ammo
        self.alive = True
    def __str__(self):
        return (f'{self.tank_name} (Armor -> {self.armor}, Ammo -> {self.ammo})')
    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print (f'{self.tank_name} fires at {enemy.tank_name}')
            enemy.target()
        else:
            print (f'{self.tank_name} has no Ammo left !')
    def target(self):
        random.seed = (os.urandom(1024))
        hit_outcomes = [True, False]
        hit_severity = [5, 10, 15, 20, 25]
        if random.choice(hit_outcomes):
            self.armor -= random.choice(hit_severity)
            print (f'{self.tank_name} is Hit !')
            if self.armor <= 0:
                self.explode()
                self.armor = 0
        else:
            print (f'{self.tank_name} has dodged the Fire !')
    def explode(self):
        self.alive = False
        print (f'{self.tank_name} has Exploded !')
    def check_if_alive(self):
        if not self.alive:
            print (f'{self.tank_name} is already Dead !')
            return 0
        else:
            return 1
