#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""main

File: main.py \n
Author: Alan Grant \n
Version: 1.0 \n
Date: 04/12/2017 \n
Class: CSCI-C 458 \n

This is the main file for the checkers game.
"""


import sys
from source import CheckersGame


# Constants for the bot's search algorithm.
SCORE = 1e9
DEPTH = 25
TIME = 10


# Implement a scoring functon here if you so choose


# run the game
if len(sys.argv) > 1:
    game = CheckersGame(sys.argv[1], SCORE, DEPTH, TIME)
else:
    game = CheckersGame('layouts/8x8.board', SCORE, DEPTH, TIME)

game.play()
