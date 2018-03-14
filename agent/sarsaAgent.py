import clr
clr.AddReference("HandEvaluator")
from HoldemHand import Hand
from System import Array, Double, String, Int64
import time
from collections import namedtuple
from enum import Enum
from holdem import PLAYER_STATE, COMMUNITY_STATE, STATE, ACTION, action_table, card_to_normal_str
import random
import numpy as np

def card_list_to_str(cards):
    s = ""
    for c in cards:
        if c == -1:
            break
        s += (card_to_normal_str(c) + " ")
    return s.strip()
    
class sarsaModel():
    def __init__(self):
        self._nothing = "test"
        self.reload_left = 2
        self.model = {"seed":831}
        self.hand_odds = 0.0
        self.lastboard = ""
        self.round = 0
        self.Q = np.zeros(4,10*9*10*3).reshape(10,9,10,3)

    def batchTrainModel(self):
        return

    def onlineTrainModel(self):
        return

    def saveModel(self, path):
        numpy.save("sarsa.npy", self.Q)
        return

    def loadModel(self, path):
        return
        
    def calcHandOdds(self, pocket, board):
        playerWins = Array[Double]([1.0]*9)
        opponentWins = Array[Double]([0.0]*9)
        Hand.HandPlayerOpponentOdds(Pocket, Board, playerWins, opponentWins)
        return float(sum(playerWins))
    
    def readState(self, state, playerid):
        call_risk = float(state.community_state.to_call)/state.community_state.totalpot
        pocket = card_list_to_str(state.player_states[playerid].hand)
        board = card_list_to_str(state.community_card)
        
        if board != self.lastboard:
            self.hand_odds = self.calcHandOdds(pocket, board)
            self.lastboard = board
            self.round += 1
        
        n_players = 0
        for p in state.player_states:
            if p.playing_hand:
                n_players += 1

    def takeAction(self, state, playerid):
        ''' (Predict/ Policy) Select Action under state'''
        self.readState(state, playerid)
        return ACTION(action_table.RAISE, state.community_state.to_call )

    def getReload(self, state):
        '''return `True` if reload is needed under state, otherwise `False`'''
        if self.reload_left > 0:
            self.reload_left -= 1
            return True
        else:
            return False