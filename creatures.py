'''
@author: Twelve
'''
#import levels
import config as c


class Creatures:
    '''
    classdocs
    '''


    def __init__(self, creatureName, creaRace, creaChar):
        '''
        Constructor
        '''
        #creature ID
        self.ID = None

        self.creaName = creatureName
        self.crColor = None

        #race name
        self.cRace = creaRace

        #display char
        self.crChar = creaChar

        #placement
        self.cooX = 0
        self.cooY = 0

    def check_tile(self, newy, newx):
        return c.gamelev.tiles[newy][newx].can_i_move()