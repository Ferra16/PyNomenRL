'''

@author: Twelve
'''
#import levels
#from config import *
import config
import mobs

#from Geng import items
import Geng.items as items
#import Geng.items

import random




class Levels(object):
    '''
    Level class. Contains levels size, tiles, etc.
    '''

    def __init__(self, levels_name):
        self.levels_name = levels_name
        self.tiles = []
        """ :type: list[list[Tiles]]  """

        #list of mobs and char on current level
        self.mob_list = []
        """ :type : list[Mob]  """
        self.char_list = []

        self.items_list = []
        """ :type : list[items]  """

        self.create_array_of_tiles(config.wcoo[0]['w'],
                                   config.wcoo[0]['h'])

        self.create_rect_wall(0, 0, 10, 20)

    def print_one_map_char(self, x, y):
        ch = self.tiles[y][x].get_tile_print_char()

        return ch

    def print_one_color_char(self, y, x):
       # ch = self.tiles[y][x].Get_Tile_Print_Char(), self.tiles[y][x].view_color, self.tiles[y][x].BGcolor
        ch = self.tiles[y][x].get_tile_print_char(), self.tiles[y][x].view_color
        return ch

    def create_array_of_tiles(self, maxx, maxy):
        for y in xrange(maxy):
            ttt = []
            for x in xrange(maxx):
                t = Tiles(x, y, ".", "WHITE")
                t.ismovable = True
                ttt.append(t)
            self.tiles.append(ttt)

    def print_map(self):
        display_strings = []

        for y in xrange(config.wcoo[0]['h']):
            screen_string = ''
            for x in xrange(config.wcoo[0]['w']):
                screen_string += self.print_one_map_char(x, y)
            display_strings.append(screen_string)
        return display_strings

    def create_rect_wall(self, y0, x0, h, w):
        for x in range(x0, (x0 + w)):
            self.tiles[y0][x].make_wall('#', "WHITE")
            self.tiles[y0 + h - 1][x].make_wall('#', "WHITE")

        for y in range(y0, (y0 + h)):
            self.tiles[y][x0].make_wall("#", "WHITE")
            self.tiles[y][x0 + w - 1].make_wall('#', "WHITE")

    def enter_mob_in_tile(self, newcoox, newcooy, mobChar ):
        return self.tiles[newcooy][newcoox].can_i_move()

    def create_mobs(self, num):
        """
         Create some mobs on the level
        """
        for n in xrange(num):
            #x = 0
            #y = 0
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            while self.tiles[y][x].isempty is False:
                x = random.randint(1, 9)
                y = random.randint(1, 9)
            mob = mobs.Mob("Orc", 'o', "GREEN", x, y)
            self.mob_list.append(mob)

    def create_items_on_level(self, kind, num):
        if kind == 'weapon':
            item = items.Weapon()
            """:type: items.Weapon  """
            #item = Geng.items.wea

            x = random.randint(1, 9)
            y = random.randint(1, 9)
            item.drop(7, 7)
            self.items_list.append(item)


    def genarate_map(self):
        pass


class Tiles(object):
    def __init__(self, x, y, print_char, char_color):


        #TODO: create item char and color variable!
        self.x = x
        self.y = y
        self.isempty = True
        self.hasitem = False
        self.hasmob = False

        self.objchar = ' '
        self.objcolor = ''

        self.print_char = print_char
        self.char_color = char_color
        self.bgcolor = "BLACK"
        self.view_color = self.char_color + '_' + self.bgcolor

        self.ismovable = True
        self.description = "Simple floor"

    def make_wall(self, pr_char, color):
        self.print_char = pr_char
        self.description = "Simple stone wall"
        self.ismovable = False

    def can_i_move(self):
        if self.ismovable is False:
            return False
        else:
            return True

    def get_tile_print_char(self):

        if self.hasitem is True or self.hasmob is True:
            return self.objchar
        elif self.isempty:
            return self.print_char
        else:
            return self.objchar

    def mob_move_in(self, mobchar, color):
        self.objchar = mobchar
        self.isempty = False
        self.ismovable = False
        self.objcolor = color
        self.view_color = self.get_tile_color(color, self.bgcolor)
        self.hasmob = True

    def mob_move_out(self):
        self.objchar = ' '
        self.objcolor = None
        self.view_color = self.get_tile_color(self.char_color, self.bgcolor)

        self.isempty = True
        self.hasmob = False
        self.ismovable = True

    def item_drop_in(self, itemchar, color):
        self.objchar = itemchar
        self.objcolor = color
        self.hasitem = True
        self.view_color = self.get_tile_color(color, self.bgcolor)

    def item_pick_up(self):
        self.objchar = ' '
        self.objcolor = None
        self.view_color = self.get_tile_color(self.char_color, self.bgcolor)
        self.hasitem = False #TODO: fix, multiple item pick up

    def get_tile_color(self, ojb_color, bg_color):
        """
        :type ojb_color: str
        :type bg_color: str
        """
        return ojb_color + '_' + bg_color

    def get_tile_info(self):
        information = 'isempy ' + str(self.isempty) + '; item ' + str(self.hasitem) + '; char ' + str(self.objchar)
        return information