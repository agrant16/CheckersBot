#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""successors

This module provides access to the Successor Generator class. This class is 
used by the checkers simulation for a checkers playing robot.

Author: Alan Grant
Version: 1.0
Date: 04/12/2017
Class: CSCI-C 458
"""


from copy import deepcopy
from time import time
from checkers_state import CheckersState


class SuccessorGenerator:
    """SuccessorGenerator
    
    The SuccessorGenerator class provides an object interface for use in 
    getting all successor states to a given CheckersState object.
    
    Attributes:
        state : The current CheckersState we are finding successors for. 
    """
    
    def __init__(self, state):
        """__init__
        
        The __init__ method is the constructor for the CheckersState class.
        
        Args:
            State (CheckersState) : The current state of the game.
        """
        self.state = state


