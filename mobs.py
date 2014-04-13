from unittest.test.test_result import __init__

__author__ = 'twelve'
from creatures import Creatures
import config as c


class Mob(Creatures):
    def __init__(self, crName, crChar, color, x, y):
        Creatures.__init__(self, crName, crName, crChar)
        self.crColor = color
        c.gamelev.tiles[y][x].mob_move_in(self.crChar, self.crColor)
        self.cooX = x
        self.cooY = y
        #c.gamelev.tiles[self.cooY][self.cooX].Mob_Move_Out()
