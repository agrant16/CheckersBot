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
     
    
    def _is_valid_move(self, successors, moves):
        """_is_valid_move
        
        The _is_valid_move function takes the player's move list and checks if 
        it repesents a legal move for the current game state.
        
        Args:
            moves (list) : A list of tuples (x,y) representing squares on the 
            board. This list is the sequence of steps 
            {start, step1, step2, ..., end} which the comprise the player's 
            move.
            successors (list) : A list of CheckersState objects representing 
            all ending states of the player's legal moves. 
        
        Returns:
            bool : True if moves represents a legal move, False otherwise.
        """
        valid = False
        generator = SuccessorGenerator(state)
        for successor in successors:
            if successor.moves == moves:
                valid = True
        return valid
        
    def _game_over(self):
        """_game_over
        
        The _game_over method is run when a terminal state has been reached. 
        A terminal state results from one of two things happening: either all 
        of one player's pieces have been removed from the board or one of the 
        players has no legal moves available. 
        """
        if state.bot_lost:
            print('CONGRATULATIONS! YOU WON THE GAME!')
        else:
            print('Unfortunately, you lost the game. '
                  'All hail our robot overlords.')

