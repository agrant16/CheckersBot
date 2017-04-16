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

``` 
      0123456789
    A _b_b_b_b_b
    B b_b_b_b_b_
    C _b_b_b_b_b
    D b_b_b_b_b_
    E __________
    F __________
    G _p_p_p_p_p
    H p_p_p_p_p_
    I _p_p_p_p_p
    J p_p_p_p_p_
```

The size of the board will vary depending on which board layout you use, but it 
will follow the same style. 'b's are pieces controlled by the bot and 'p's are 
pieces controlled by the player. If a piece is kinged th letter representng 
that piece will be a capital letter.  

The human player always starts first and to input a move you simply type the 
coordinates of the piece you want to move and the square you want to move the 
piece to. For example, when prompted to choose your move typing:  
```G3 F4```

will move the piece located at square G3 to square F4.  

You perform jumps the same way and to perform multiple jumps you simply add 
the need squares. For example if we have the following layout:

``` 
     012345
   A ______
   B __b___
   C ______
   D ____b_
   E _____p
   F ______
```
and we type in the following move:

```E5 C3 A1```

our piece will jump both of the bot's pieces and win the game.   

And that's all there really is to playing the game.  

## The Algorithm

This bot uses an iterative deepening depth-first search (IDDFS) with a minimax 
algorithm for decision making. It also uses Alpha-Beta pruning to avoid 
travelling paths the bot will never choose. The algorithm was inpsired by a 
[blog post](https://kartikkukreja.wordpress.com/2015/07/12/creating-a-bot-for-checkers/)
 from Kartik Kukreja.  

[Iterative Deepening Depth-First Searcih](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)


If you open up main.py you'll see some constants at the top:

```
    SCORE
    DEPTH
    TIME
```

These constants are used by the bot to perform it's search algorithm. SCORE 
is the max score for the minimax function, DEPTH is the max depth for the 
search algorithm, and TIME is the max time to perform the search. Feel free 
to change the values and play around. Right now they work fairly well.  

The bot also has a built in scoring function which it uses by default. You 
can change the algorithm the bot uses if you want. Simply implement it where 
noted in the file and then pass it in when creating the new CheckersGame 
object to override the default argument.  

For example, if I created a new scoring function called 'best_ever', I would 
change the calls to the CheckersGame constructors like so:

```game = CheckersGame(sys.argv[1], SCORE, DEPTH, TIME, bot_func=best_ever)```

```game = CheckersGame('source/layouts/8x8.board', SCORE, DEPTH, TIME, bot_func=best_ever)```

This would cause the game to use your custom scoring function. 

