#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""checkers_bot

File: checkers_bot.py \n
Author: Alan Grant \n
Version: 1.0 \n
Date: 04/14/2017 \n
Class: CSCI-C 458 \n

This module provides access to the CheckersBot class. The CheckersBot class 
takes a game state and attempts to find the bot's best move based on that game 
state. 
"""


from time import time
from successors import SuccessorGenerator
from checkers_state import CheckersState

class CheckersBot:
    """CheckersBot
    
    The CheckersBot class is used to control a bot when playing the checkers 
    game. To decide on which move it should make it performs a minimax 
    iterative deepening depth-first search with Alph-Beta pruning.
    
    Attributes:
        state (CheckersState) : The current state of the game.
        max_score (int) : The upper limit for the minimax score.
        max_depth (int) : The max depth for the bot's iddfs algorithm.
        max_time (double) : The max time in seconds for the bot to search.
        eval_func (function) : The scoring function for the bot to use. 
        start_time (int) : The start time of the bot's search.
    """
    
    def __init__(self, state, max_score, max_depth, max_time, eval_func):
        """ __init__
        
        The __init__ function is the constructor for the CheckersBot.
        
        Args:
            state (CheckersState) : The current state of the game.
            max_score (int) : The max score for the bot's minimax search.\n
            max_depth (int) : The max depth for the bot's IDDFS search.\n
            max_time (float) : The max search time for the bot's search.\n 
            eval_func (function) : The evaluation function used for scoring of 
            states found by the bot's search.\n
        """
        self.state = state
        self.max_score = max_score
        self.max_depth = max_depth
        self.max_time = max_time
        self.eval_func = eval_func
        self.start_time = 0
        
    def _max_value(self, state, alpha, beta, depth):
        """_max_value
        
        The _max_value function is used by the minimax algorithm to attempt to 
        find the best (highest value) move from all the successors of the 
        current state.
        
        Args: 
            state (CheckersState) : The current state of the game. 
            alpha (int) : The current alpha pruning score.
            beta (int) : The current beta pruning score.
            depth (int) : The current depth of the search algorithm. 
        
        Return:
            int : The max score for the successor states.
        """
        val = -self.max_score
        max_gen = SuccessorGenerator(state)
        for successor in max_gen.successors():
            val = max(val, self._alpha_beta_search(
                      successor, alpha, beta, depth))
            if val >= beta: 
                return val
            alpha = max(alpha, val)
        return val

    def _min_value(self, state, alpha, beta, depth):
        """_min_value
        
        The _min_value function is used by the minimax algorithm to attempt to 
        find the worst (least value) move from all the successors of the 
        current state.
        
        Args: 
            state (CheckersState) : The current state of the game. 
            alpha (int) : The current alpha pruning score.
            beta (int) : The current beta pruning score.
            depth (int) : The current depth of the search algorithm. 
        
        Return:
            int : The min score for the successor states.
        """
        val = self.max_score
        min_gen = SuccessorGenerator(state)
        for successor in min_gen.successors():
            val = min(val, self._alpha_beta_search(successor, alpha, beta, depth - 1))
            if val <= alpha: 
                return val
            beta = min(beta, val)
        return val
        
    def _alpha_beta_search(self, state, alpha, beta, depth):
        """_alpha_beta_search
        
        The _alpha_beta_search function is used by the minimax algorithm to 
        attempt to prune out tree branches of the search tree for which the 
        result would be one we will likely never choose.
        
        Args: 
            state (CheckersState) : The current state of the game. 
            alpha (int) : The current alpha pruning score.
            beta (int) : The current beta pruning score.
            depth (int) : The current depth of the search algorithm. 
        
        Return:
            int : The score for the given state.
        """
        if state.is_terminal():
            return (self.max_score if state.bots_move != state.bot_lost else -self.max_score)
            
        if depth <= 0 or time() - self.start_time > self.max_time:
            return self.eval_func(state)
        
        return (self._max_value(state, alpha, beta, depth) if state.bots_move
                == True else self._min_value(state, alpha, beta, depth))

    def _iterative_deepening_dfs(self):
        """_iterative_deepening_dfs
        
        The _iterative_deepening_dfs searches the tree of successor states 
        looking for the best move. It uses a minimax algorithm with Alpha-Beta 
        pruning to ignore branches of the tree where we will never choose the 
        result from.
        
        Returns:
            bestMove (CheckersState) : A CheckersState representing the end 
            state of the "best" move the bot could make. 
        """
        self.start_time = time()
        bestMove = None
        generator = SuccessorGenerator(self.state)
        
        for depth in range(1, self.max_depth):
            print(depth)
            if time() - self.start_time > self.max_time:
                break
            val = -self.max_score
            for successor in generator.successors():
                score = self._alpha_beta_search(successor, -self.max_score, self.max_score, depth)
                if score > val:
                    val, bestMove = score, successor
        return bestMove
        
    def update_state(self, new_state):
        """update_state
        
        The update_state function does exactly what it says i does: updates 
        the current state to a new state.
        
        Args:
            new_state (CheckersState) : The most recent state of the game.
        """
        self.state = new_state
    
    def get_move(self):
        """get_move
        
        The get_move function is a public helper function which simply calls 
        the iddfs function.
        
        Returns:
            CheckersState : The state object representing the end state of 
            what the bot has determined is the "best" move.
        """
        return self._iterative_deepening_dfs()
