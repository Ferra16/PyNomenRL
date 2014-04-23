import config

__author__ = 'Twelve'

#from unicurses import *

#from unicurses import *
#import Geng
#from Geng import uni_display
#from Geng import *
from Geng.uni_display import *
#import levels
from player import *
import config as cf

stdscr = initscr()

noecho()
cbreak()
curs_set(0)
keypad(stdscr, True)
clear()

stopGame = True
refresh()

GameScreen = GameScreen()

cf.gamelev = levels.Levels("Dungeon")
GameScreen.uni_disp_init()

# c.gamelev.genarate_map()

c.AddBattleLog("hello")

GameScreen.Dungeon_Name = config.gamelev.levels_name

#_pl = Player()
c.gamelev.create_mobs(2)
#c.gamelev.create_items_on_level('weapon', 1)
c.gamelev.create_player()

while stopGame:
    #addstr("Ok, start")

    #GameScreen.Current_Level_Printed_Map = config.gamelev.print_map()

    GameScreen.draw_screens()

    #lev.create_rooms(0, 0, getmaxyx(config.scrns[0])[1], getmaxyx(config.scrns[0])[0])
    k = getch()
    if k == CCHAR('q'):
        stopGame = False

    elif k == KEY_LEFT or k == CCHAR('4'):
        c.pl.Move('w')

    elif k == CCHAR('7'):
        c.pl.Move('nw')

    elif k == KEY_UP or k == CCHAR('8'):
        c.pl.Move('n')

    elif k == CCHAR('9'):
        c.pl.Move('ne')

    elif k == KEY_RIGHT or k == CCHAR('6'):
        c.pl.Move('e')

    elif k == CCHAR('3'):
        c.pl.Move('se')

    elif k == KEY_DOWN or k == CCHAR('2'):
        c.pl.Move('s')

    elif k == CCHAR('1'):
        c.pl.Move('sw')




    elif k == CCHAR('l'):

        stoplook = True
        x = 8
        y = 7
        curs_set(True)

        while stoplook:
            g = getch()
            if g == CCHAR('q'):
                stoplook = False

            elif g == KEY_LEFT or g == CCHAR('4'):
                x -= 1
            elif g == KEY_RIGHT:
                x += 1
            elif g == KEY_UP:
                y -= 1
            elif g == KEY_DOWN:
                y += 1

            c.AddBattleLog(c.gamelev.tiles[y][x].get_tile_info())
            wclear(c.scrns[c.nos["scr_log"]])
            wclear(c.scrns[c.nos["scr_map"]])
            move(y, x)
            GameScreen.print_BLOG()
            GameScreen.color__draw_map()
            wrefresh(c.scrns[c.nos["scr_log"]])
            wrefresh(c.scrns[c.nos["scr_map"]])
            #GameScreen.draw_screens()
            #elif g == CCHAR('7'):
            #    _pl.Move('nw')

"""
                    elif k == KEY_UP or k == CCHAR('8'):
                    _pl.Move('n')

    elif k == CCHAR('9'):
        _pl.Move('ne')

    elif k == KEY_RIGHT or k == CCHAR('6'):
        _pl.Move('e')

    elif k == CCHAR('3'):
        _pl.Move('se')

    elif k == KEY_DOWN or k == CCHAR('2'):
        _pl.Move('s')

    elif k == CCHAR('1'):
        _pl.Move('sw')

"""

clear()
addstr("Stop for now, later we'll see.")

endwin()