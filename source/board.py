#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""board

This module provides access to the CheckersBoard class. This class is used by
the checkers simulation for a checkers playing robot.

Author: Alan Grant
Version: 1.0
Date: 04/12/2017
Class: CSCI-C 458
"""
import sys

class CheckersBoard:
    """CheckersBoard
    
    The CheckersBoard class represents a checkers board. It is a simple class
    for storing the layout of a checkers board. It provides an easy way to
    print the board by using the magic string method.
    
    Attributes:
        layout (str) : The file path to file containing the board layout.\n
        board (list) : A list of strings which represents the layout of the
        board. 
    """
    
    def __init__(self, layout):
        """__init__
        
        The __init__ method is the constructor for the CheckersBoard class. It
        attempts to open the layout file and read in the board layout to
        initialize the board.
        
        Args:
            layout (str) : The file path to the layout file. 
        """
        self.layout = layout
        self.reset()


    
    def __str__(self):
        """__str__
        
        The __str__ method returns a string representation of the class.
        """
        
        s = '  ' + ''.join(str(i) for i in range(len(self.board[0]))) + '\n'
        
        for i, row in enumerate(self.board):
            s += chr(i + 65) + ' ' + row + '\n'
        return s
        
        
    def reset(self):
        """reset
        
        The reset function returns the game board to the original default layout.
        
        Args:
            layout (str) : The file path to the file containing the default
            board layout. 
        
        """
        try:
            f = open(self.layout, 'r') 
        except IOError as err:
            print(err)
            sys.exit()
            
        with f:
            self.board = [line.strip() for line in f]

if __name__ == '__main__':
    board = CheckersBoard('source/layouts/6x6.board')
    print(board)
