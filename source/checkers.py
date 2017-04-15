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
    """CheckersGame
    
    The CheckersGame class controls the game of checkers being played. 
    
    Attributes:
        board (CheckersBoard) : The board object storing information of the 
        current board layout.\n
        bot_score (int) : The max score for the bot's minimax search.\n
        bot_depth (int) : The max depth for the bot's IDDFS search.\n
        bot_time (float) : The max search time for the bot's search.\n 
        bot_func (function) : The evaluation function used for scoring of 
        states found by the bot's search.\n
        board_size (int) : The current size of the board layout being used.\n
        player_gen (SuccessorGenerator) : The generator used to find legal 
        moves that the human player can make.\n
        bot (CheckersBot) : The checkers bot. 
    
    """
    def __init__(self, layout, bot_score=None, bot_depth=None, bot_time=None, bot_func=None):
        """ __init__
        
        The __init__ function is the constructor for the CheckersGame Class.
        
        Args:
            layout (str) : File path to the file containing the desired board 
            layout.\n
            bot_score (int) : The max score for the bot's minimax search.\n
            bot_depth (int) : The max depth for the bot's IDDFS search.\n
            bot_time (float) : The max search time for the bot's search.\n 
            bot_func (function) : The evaluation function used for scoring of 
            states found by the bot's search.\n
        """
        self.board = CheckersBoard(layout)
        self.bot_score = bot_score
        self.bot_depth = bot_depth
        self.bot_time = bot_time
        self.bot_func = bot_func
        self.board_size = len(self.board.board)
        self.bot = CheckersBot
        self.player_gen = None
        self.bot = None  
        
    
    def _get_player_move(self):
        """_get_player_move
        
        The _get_player_move method takes the player's move list as input from 
        stdin.
        
        Returns:
            list : A list of tuples (x,y) representing squares on the board. 
            This list is the sequence of steps {start, step1, step2, ..., end} 
            which the comprise the player's move.
        """
        print('It is the player\'s turn. Please input your move.')
        st = input().split()
        return [(int(ord(x[0]) - 65), int(x[1])) for x in st]
 
