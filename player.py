__author__ = 'Twelve'
import levels
import config as c
import creatures

class Player(creatures.Creatures):
    def __init__(self):
        self.NAME = "Player"
        self.print_char = '@'
        self.color = "WHITE"

        self.raceName = "Ogroid"

        self.cooX = 5
        self.cooY = 5

        c.gamelev.tiles[self.cooY][self.cooX].mob_move_in(self.print_char, self.color)


    def Move(self, direction):
        newcooX = self.cooX
        newcooY = self.cooY

        if direction == 'n': newcooY -= 1

        elif direction == 'ne':
            newcooX += 1
            newcooY -= 1

        elif direction == 'e': newcooX += 1

        elif direction == 'se':
            newcooX += 1
            newcooY += 1

        elif direction == 's': newcooY += 1

        elif direction == 'sw':
            newcooX -= 1
            newcooY += 1

        elif direction == 'w': newcooX -= 1

        elif direction == 'nw':
            newcooX -= 1
            newcooY -= 1

        if self.check_tile(newcooY, newcooX):
            c.gamelev.tiles[newcooY][newcooX].mob_move_in(self.print_char, self.color)
            c.gamelev.tiles[self.cooY][self.cooX].mob_move_out()

            self.cooX = newcooX
            self.cooY = newcooY
        else:
            c.AddBattleLog("Bump")

