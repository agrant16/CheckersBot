#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""checkers

File: checkers.py \n
Author: Alan Grant \n
Version: 1.0 \n
Date: 04/12/2017 \n
Class: CSCI-C 458 \n

This module provides access to the CheckersGame class. The CheckersGame 
class controls the logic for running a checkers simulation. 
"""


import sys
from .board import CheckersBoard
from .successors import SuccessorGenerator
from .checkers_state import CheckersState
from .checkers_bot import CheckersBot

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
    def __init__(self, layout, bot_score, bot_depth, bot_time, 
                 bot_func=None):
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
        self.board_size = len(self.board.board)
        self.bot = CheckersBot
        self.player_gen = None
        self.bot = None  
        if bot_func == None:
            self.bot_func = self.eval_func_1
        else:
            self.bot_func = bot_func
        

    def eval_func_1(state):
        """eval_func_1
        
        This is a generic scoring function for a CheckersState. It simply 
        assigns a score to each piece on the board and sums that score. 
        
        Args:
            state (CheckersState) : The current game state.
        
        Returns:
            score (int) : A score based on how many pieces are on the board in 
            the current state.
        """
        score = 0
        for row in state.board:
            for square in row:
                if square == 'b':
                    score += 1.0
                elif square == 'B':
                    score += 1.5
                elif square == 'p':
                    score -= 1.0
                elif square == 'P':
                    score -= 1.5

        return score
        

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
        new_board = None
        for successor in successors:
            if successor.moves == moves:
                valid = True
                new_board = successor.board
        return valid, new_board
       
        
    def _game_over(self, state):
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
         
    def _bots_move_to_str(self, moves):
        """_bots_move_to_str
        
        The _bots_move_to_str method returns a string representation of the 
        bot's move in the coordinate system of the game board.
        
        Returns:
            str : The bot's move as a string. 
        """
        s = ''
        for x,y in moves:
            s += chr(x + 65) + str(y) + ' '
        return s + '\n'
        
          
    def play(self):
        """play
        
        The play function begins the game. It instantiates player_gen and bot 
        with new objects. It uses a while True loop which continues until a 
        terminal state has been reached. 
        """
        state = CheckersState(self.board.board, False, [], self.board_size)
        self.player_gen = SuccessorGenerator(state)
        self.bot = CheckersBot(state, 
                               self.bot_score, 
                               self.bot_depth, 
                               self.bot_time, 
                               self.bot_func)
        while True:
            print(self.board)

            # The player's move
            successors = self.player_gen.successors()
            
            if len(successors) == 0:
                self._game_over(state)
                break
                
            moves = self._get_player_move()
            valid, new_board = self._is_valid_move(successors, moves)
            
            if not valid:
                print('That is not a legal move. Please attempt another move')
                continue
            else:
                self.board.board = new_board

            print('\n' + str(self.board))
            
            state = CheckersState(self.board.board, True, [], self.board_size)
            
            if state.is_terminal():
                self._game_over(state)
                break
            
            # The bot's move
            print('It is the bot\'s move. Waiting on bot...')
            self.bot.update_state(state)
            bots_move = self.bot.get_move()
            bot_move_str = self._bots_move_to_str(bots_move.moves)
            print('The bot has chosen the following move: \n' +
                   bot_move_str)

            if bots_move == None or bots_move.is_terminal():
                self._game_over(state)
                break
            else:
                self.board.board = bots_move.board  
            
            self.player_gen.update_state(CheckersState(
                                    self.board.board, 
                                    False, [], self.board_size))
