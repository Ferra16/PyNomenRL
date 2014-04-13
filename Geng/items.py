__author__ = 'Twelve'

import random

import config as c

weapon_kind = ['sword', 'mace']
weapon_suffix = ['of might', 'of horror', 'of magic']


item_type = ['weapon', 'armor']


class Item(object):
    def __init__(self, kind):

        self.name = None
        self.weight = None
        self.durability = None
        self.kind = kind


        self.color = None

        self.dropped = True

        self.cooX = None
        self.cooY = None

    def drop(self, y, x):
        self.cooY = y
        self.cooX = x
        self.dropped = True
        c.gamelev.tiles[y][x].item_drop_in(self.char, self.color)


class Weapon(Item):
    def __init__(self):
        Item.__init__(self, random.choice(weapon_kind))
        self.name = self.kind + random.choice(weapon_suffix)
        self.char = '('
        self.color = 'RED'