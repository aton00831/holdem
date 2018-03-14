from collections import namedtuple
from enum import Enum
from holdem import PLAYER_STATE, COMMUNITY_STATE, STATE, ACTION, action_table
import random

class allRaiseModel():
    def __init__(self):
        self._nothing = "test"
        self.reload_left = 2
        self.model = {"seed":831}

    def batchTrainModel(self):
        return

    def onlineTrainModel(self):
        return

    def saveModel(self, path):
        return

    def loadModel(self, path):
        return

    def takeAction(self, state, playerid):
        ''' (Predict/ Policy) Select Action under state'''
        return ACTION(action_table.RAISE, state.community_state.to_call )

    def getReload(self, state):
        '''return `True` if reload is needed under state, otherwise `False`'''
        if self.reload_left > 0:
            self.reload_left -= 1
            return True
        else:
            return False