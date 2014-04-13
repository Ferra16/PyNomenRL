'''
@author: Twelve
'''
from unicurses import *

import config as c

#import levels
#from levels import *



class GameScreen(object):
    def __init__(self):
        self.Current_Level_Printed_Map = None
        self.Dungeon_Name = None

        self.Battle_Log = c.Battle_Log
        """ :type : list [str] """

    def uni_disp_init(self):
        start_color()
        init_pair(1, COLOR_WHITE, COLOR_BLACK)
        init_pair(2, COLOR_CYAN, COLOR_BLACK)  # used for the walls
        init_pair(3, COLOR_RED, COLOR_BLACK)  # used for the statues
        init_pair(4, COLOR_GREEN, COLOR_BLACK)  # used for low hit points
        init_pair(5, COLOR_YELLOW, COLOR_BLACK)  # used for the status bar

        c.colors_ingame['WHITE_BLACK'] = 1
        c.colors_ingame['CYAN_BLACK'] = 2
        c.colors_ingame['RED_BLACK'] = 3
        c.colors_ingame['GREEN_BLACK'] = 4
        c.colors_ingame['YELLOW_BLACK'] = 5


        #scr_map = newwin(19, 60, 0, 0)
        #scr_log = newwin(7, 60, 18, 0)
        #scr_stats = newwin(19, 21, 0, 59)

        scr_map = newwin(c.wcoo[0]['h'],
                         c.wcoo[0]['w'],
                         c.wcoo[0]['y'],
                         c.wcoo[0]['x'])

        scr_log = newwin(c.wcoo[1]['h'],
                         c.wcoo[1]['w'],
                         c.wcoo[1]['y'],
                         c.wcoo[1]['x'])

        scr_stats = newwin(c.wcoo[2]['h'],
                           c.wcoo[2]['w'],
                           c.wcoo[2]['y'],
                           c.wcoo[2]['x'])

        scr_Lev_Name = newwin(c.wcoo[3]['h'],
                              c.wcoo[3]['w'],
                              c.wcoo[3]['y'],
                              c.wcoo[3]['x'])

        c.scrns.append(scr_map)
        c.scrns.append(scr_log)
        c.scrns.append(scr_stats)
        c.scrns.append(scr_Lev_Name)

    def set_current_level(self, level):
        self.CurrentLevel = level

    def draw_screens(self):
        for scr in c.scrns:
            #box(scr, 0, 0)
            # Display map screen
            wclear(scr)
        #draw dungeon name
        self.draw_dungeon_name()
        #draw Map
        #self.draw_map()
        self.color__draw_map()

        self.print_BLOG()



        for scr in c.scrns:
            #box(scr, 0, 0)
            # Display map screen
            wrefresh(scr)

    def print_BLOG(self):
        win_height = c.wcoo[c.nos["scr_log"]]['h']
        lastElem = c.Battle_Log[-win_height:]
        lastElem.reverse()
        y = 0
        for str_in_log in lastElem:
            mvwaddstr(c.scrns[c.nos["scr_log"]], y, 0, str_in_log)
            y += 1

    def draw_map(self):
        yscr1 = 0
        for prstr in self.Current_Level_Printed_Map:
            mvwaddstr(c.scrns[c.nos["scr_map"]], yscr1, 0, prstr)
            yscr1 += 1

    def draw_dungeon_name(self):
        mvwaddstr(c.scrns[3], 0, 0, self.Dungeon_Name)

    def color__draw_map(self):
        for y in xrange(c.wcoo[0]['h']):
            for x in xrange(c.wcoo[0]['w']):
                color_char = c.gamelev.print_one_color_char(y, x)
                Tile_Ch = color_char[0]
                Tile_Ch_Color = color_char[1]
                #Tile_Bg_Color = color_char[2]

                #start_color()
                #init_pair(1, c.colors[Tile_Ch_Color], c.colors[Tile_Bg_Color])

                wattron(c.scrns[c.nos["scr_map"]],COLOR_PAIR(c.colors_ingame[Tile_Ch_Color]))
                mvwaddstr(c.scrns[c.nos["scr_map"]], y, x, Tile_Ch)
                #wattroff(c.scrns[c.nos["scr_map"]],COLOR_PAIR(1))

                #wattron(c.scrns[c.nos["scr_map"]],COLOR_PAIR(1111))
                #mvwaddstr(c.scrns[c.nos["scr_map"]], y, x, Tile_Ch)
                #wattroff(c.scrns[c.nos["scr_map"]],COLOR_PAIR(1111))

