'''
@author: Twelve
'''
#from unicurses import *
import levels

colors_ingame = {}
""" :type : dict[str, int] """

colors = {"GREEN" : "COLOR_GREEN",
          "WHITE" : "COLOR_WHITE",
          "YELLOW" : "COLOR_YELLOW",
          "BLACK" : "COLOR_BLACK"}

nos = {
   "scr_map" : 0,
   "scr_log" : 1,
   "scr_stats" : 2,
   "scr_Lev_Name" : 3
}

scrns = []




#  scr_map = newwin(19, 60, 0, 0)
# scr_log = newwin(7, 60, 18, 0)
# scr_stats = newwin(19, 21, 0, 59)


wcoo = []
""" :type: list[dict[str, int]]  """


wcoo.append({'h': 18, 'w': 59, 'x': 0, 'y': 1})
wcoo.append({'h': 6, 'w': 80, 'x': 0, 'y': 19})
wcoo.append({'h': 19, 'w': 21, 'x': 59, 'y': 0})
wcoo.append({'h': 1, 'w': 59, 'x': 0, 'y': 0})

pl = None
""" :type : Player """

gamelev = None
""" :type gamelev: Levels  """

Battle_Log = []
""" :type : list[str] """


def AddBattleLog(text):
    Battle_Log.append(text)

#win_coords.append({'h': 19, 'w': 60, 'x': 0, 'y': 0})
#win_coords.append(dict(h=18, w=59, x=0, y=0))

