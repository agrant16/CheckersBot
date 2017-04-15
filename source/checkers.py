#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""checkers

File: checkers.py
Author: Alan Grant
Version: 1.0
Date: 04/12/2017
Class: CSCI-C 458

This module provides access to the CheckersGame class. The CheckersGame 
class controls the logic for running a checkers simulation. 
"""


import sys
from board import CheckersBoard
#from successors import SuccessorGenerator
#from checkers_state import CheckersState
#from checkers_bot import CheckersBot

class CheckersGame:

    def __init__(self, layout, bot_score=None, bot_depth=None, bot_time=None, bot_func=None):
        self.board = CheckersBoard(layout)
        self.bot_score = bot_score
        self.bot_depth = bot_depth
        self.bot_time = bot_time
        self.bot_func = bot_func
        self.board_size = len(self.board.board)
        self.bot = CheckersBot
        self.player_gen = SuccessorGenerator(   
        
    

