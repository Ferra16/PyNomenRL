'''

@author: Twelve
'''
#import levels
#from config import *
import config as c
import mobs
import player

import Geng.items as items


import random


class Levels(object):
    """    Level class. Contains levels size, tiles, etc.
    """

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

       #Generate map
        self.create_array_of_tiles(c.wcoo[0]['w'],
                                   c.wcoo[0]['h'])
        self.genarate_map()

        #self.create_rect_wall(0, 0, 10, 20)

    def print_one_map_char(self, x, y):
        ch = self.tiles[y][x].get_tile_print_char()

        return ch

    def print_one_color_char(self, y, x):
        ch = self.tiles[y][x].get_tile_print_char()
        return ch

    def create_array_of_tiles(self, maxx, maxy):
        """
        Create a map of tiles in given size (currently only less then size of map window.
        @param maxx: Max X coo
        @param maxy: Max Y coo
        """
        for y in xrange(maxy):
            ttt = []
            for x in xrange(maxx):
                t = Tiles(x, y, "#", "WHITE")
                t.make_wall('#', "WHITE")
                ttt.append(t)
            self.tiles.append(ttt)

    def print_map(self):
        display_strings = []

        for y in xrange(c.wcoo[0]['h']):
            screen_string = ''
            for x in xrange(c.wcoo[0]['w']):
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

    #def enter_mob_in_tile(self, newcoox, newcooy, mobChar):
    #    return self.tiles[newcooy][newcoox].can_i_move()

    def create_mobs(self, num):
        """
        Create some mobs on the level
        @type num: Mob number
        """
        for n in xrange(num):
            #x = 0
            #y = 0
            #x = random.randint(1, 9)
            #y = random.randint(1, 9)
            #x, y = self.find_empty_tiles()

            y, x = self.find_place_for_mob()
            mob = mobs.Mob("Orc", 'o', "GREEN", x, y)
            self.mob_list.append(mob)

    def create_player(self):
        y, x = self.find_place_for_mob()
        c.pl = player.Player(y, x)



    def create_items_on_level(self, kind, num):
        if kind == 'weapon':
            item = items.Weapon()
            """:type: items.Weapon  """
            #item = Geng.items.wea

            x = random.randint(1, 9)
            y = random.randint(1, 9)
            item.drop(7, 7)
            self.items_list.append(item)

    def find_empty_tiles(self):

        height = c.wcoo[0]['h'] - 2
        width = c.wcoo[0]['w'] - 2

        x = random.randint(1, width)
        y = random.randint(1, height)
        # x = random.randint(1, c.wcoo[0]['w']) - 2
        # y = random.randint(1, c.wcoo[0]['h']) - 2
        while self.tiles[y][x].iswall:
            x = random.randint(1, width)
            y = random.randint(1, height)

        return x, y

    def find_place_for_mob(self):
        has_floor = []
        for tileline in self.tiles:
            for tile in tileline:
                if tile.iswall is not True and tile.ismovable:
                    has_floor.append((self.tiles.index(tileline), tileline.index(tile)))
        y, x = random.choice(has_floor)
        return y, x

    def genarate_map(self):
        """
        Maze generator.
        @return: None
        """


        height = c.wcoo[0]['h'] - 2
        width = c.wcoo[0]['w'] - 2

        x = random.randint(5, width)
        y = random.randint(3, height)

        self.tiles[y][x].make_floor('.', "WHITE")


        x1 = x
        y1 = y

        MAX_FLOOR_TILES = 350
        where_to = ['n', 'w', 's', 'e']

        tilecount = 0

        #f = open('ww1', 'w')
        #text = ['x0=', x, 'y0=', y, '\n']

        #f.write(str(text))
        #f.write('\n')
        while tilecount < MAX_FLOOR_TILES:
            flag_ok = False
            dice = random.choice(where_to)
            if dice == 'n':
                y1 = y + 1
            elif dice == 'w':
                x1 = x - 1
            elif dice == 's':
                y1 = y - 1
            elif dice == 'e':
                x1 = x + 1

            if x1 < 1 or x1 > width:
                x1 = x
                flag_ok = True
            elif y1 < 1 or y1 > height:
                y1 = y
                flag_ok = True
            #elif self.tiles[y1][x1].iswall is False:
             #   flag_ok = True
                #x1 = x
                #y1 = y

            x = x1
            y = y1


            if flag_ok is False and \
               self.tiles[y][x].iswall is True:
                self.tiles[y][x].make_floor('.', "WHITE")
                tilecount += 1
            text1 = ['x ', x, 'y ', y, 'x1', x1, 'y1', y1, str(flag_ok), tilecount]
            #f.write(str(text1))
            #f.write('\n')
        #f.close()











class Tiles(object):
    def __init__(self, x, y, print_char, char_color):

        self.x = x
        self.y = y
        self.isempty = True
        self.hasitem = False
        self.hasmob = False
        self.iswall = False

        #mob and PC display
        self.mobchar = ' '
        self.mobcolor = ''
        #item display
        self.objchar = ' '
        self.objcolor = ''

        self.print_char = print_char
        self.tile_color = char_color
        self.bgcolor = "BLACK"
        self.view_color = self.tile_color + '_' + self.bgcolor

        self.ismovable = True
        self.description = "Simple floor"

    def make_wall(self, pr_char, color):
        self.print_char = pr_char
        self.description = "Simple stone wall"
        self.ismovable = False
        self.iswall = True

    def make_floor(self, pr_char, color):
        """
        Makes floor in the current tile.

        @param pr_char: print char of floor ('.' by default)
        @param color: color string
        @return: None
        """
        self.print_char = pr_char
        self.description = "Simple floor"
        self.ismovable = True
        self.iswall = False
        self.tile_color = color

    def can_i_move(self):
        if self.ismovable is False:
            return False
        else:
            return True

    def get_tile_print_char(self):

        color = None
        char = None
        if self.hasmob is True:
            color = self.mobcolor
            char = self.mobchar
        elif self.hasitem is True:
            color = self.objcolor
            char = self.objchar
        #elif self.iswall or self.isempty:
        elif self.iswall:
            char = self.print_char
            color = self.tile_color
        else:
            char = self.print_char
            color = self.tile_color

        color = self.get_tile_color(color, self.bgcolor)
        return char, color

    def mob_move_in(self, mobchar, color):
        """ Tells tile that mob or player moves in.
        @param mobchar: Mob display character.
        @param color: Mob character color (foreground).
        """
        self.mobchar = mobchar
        self.isempty = False
        self.ismovable = False
        self.mobcolor = color
        self.view_color = self.get_tile_color(color, self.bgcolor)
        self.hasmob = True

    def mob_move_out(self):
        self.mobchar = ' '
        self.mobcolor = None
        self.view_color = self.get_tile_color(self.tile_color, self.bgcolor)

        self.isempty = True
        self.hasmob = False
        self.ismovable = True

    def item_drop_in(self, itemchar, color):
        self.objchar = itemchar
        self.objcolor = color
        self.hasitem = True
        self.view_color = self.get_tile_color(color, self.bgcolor)

    def item_pick_up(self):
        self.mobchar = ' '
        self.mobcolor = None
        self.view_color = self.get_tile_color(self.tile_color, self.bgcolor)
        self.hasitem = False 
        #TODO: fix, multiple item pick up

    def get_tile_color(self, ojb_color, bg_color):
        """
        Return full tile color (foreground and background)
        @type self: Tiles
        @type ojb_color: str
        @type bg_color: str
        """
        return ojb_color + '_' + bg_color

    def get_tile_info(self):
        information = 'isempy ' + str(self.isempty) + '; item ' + str(self.hasitem) + '; iswall? ' + str(self.iswall)
        return information