#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""checkers_state.py

This module provides access to the CheckersState class. This class is used by
the checkers simulation for a checkers playing robot. It is a state 
representation of the game board and player turn. 

Author: Alan Grant
Version: 1.0
Date: 04/12/2017
Class: CSCI-C 458
"""

class CheckersState:
    '''CheckersState represents a board state for a checkers game.

    Attributes:
        board : A list of strings which represent the state of the board.
        blacks_move : True if it is black's (the bot's) move.
        moves : A list of coordinates representing the sequence of moves. 
        size : Size of the board. i.e. if the size is 8 then the board is 8x8.
        bot_lost (bool) : True if the state is terminal and the bot has lost,
        False otherwise. 
    '''
    
    def __init__(self, board, bots_move, moves, size):
        """__init__
        
        The __init__ method is the constructor for the CheckersState class. It
        creates a CheckersState object based on the information given. 
        
        Args:
            board (list) : A list of strings representing the current state of 
            the game board.\n 
            bots_move (bool) : True if it is the bot's move, False otherwise.\n
            moves (list) : A list of tuples (x, y) representing the squares in 
            the proposed move.\n
            size (int) : The size of the checkers board. A size of 6 is a 6x6 
            board.
        """
        self.board = board
        self.bots_move = bots_move
        self.moves = moves
        self.size = size
        self.bot_lost = False
        
    def is_terminal(self):
        '''is_terminal
        
        The is_terminal method detects if all of one color's pieces have been
        eliminated. This is a terminal state for the game.
        
        Returns:
            bool : True if a terminal state has been reached, False otherwise.
        '''
        black_exists, white_exists = False, False
        for row in self.board:
            for square in row:
                if square == 'b' or square == 'B':
                    bot_exists = True
                elif square == 'p' or square == 'P':
                    player_exists = True
                if bot_exists and player_exists:
                    return False
        self.bot_lost = player_exists
        return True

               

