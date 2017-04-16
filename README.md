# CheckersBot
**Team Members**: Alan Grant, Timothy Spalding, John Karr  
**Class**: CSCI-458  
**School**: Indiana University Southeast  
**Updated**: 04/15/2017  

This repository is a checkers simulation developed as part of the CheckersBot 
project in CSCI-C 458: Intelligent Robots and Indiana University Southeast. 
The goal of this project is to develop a robotic system capable of playing 
a simplified version of checkers. The overall project consists of three 
subsystems: a decision maker, a computer vision system, and a robotic system.  

The code found in this repository is part of the decision maker subsystem. It 
is built using an iterative deepening depth-first minimax search with 
Alpha-Beta pruning. This repository contains a fully functional checkers game. 
Instructions for playing can be found below. 

## How to Play

To play the game simply clone the repository and run main.py from the 
terminal when inside the root folder of the repository. i.e. What the 
repository would label the CheckersBot folderThe code is Python3 so you'll 
want to make sure you have it installed. In the source/layouts folder you can 
find several .board files which hold layouts for boards of size 4x4, 6x6, 8x8, 
10x10, and 12x12. If you want to use one of the board layouts simply put the 
filepath to that .board file as a command line argument. For example the 
following command would begin the game with a 10x10 board:

```python3 main.py source/layouts/10x10.board```

Once the game has begun the current board state will printed to stdout in the 
following format:  

```  0123456789
    A _b_b_b_b_b
    B b_b_b_b_b_
    C _b_b_b_b_b
    D b_b_b_b_b_
    E __________
    F __________
    G _p_p_p_p_p
    H p_p_p_p_p_
    I _p_p_p_p_p
    J p_p_p_p_p_```


