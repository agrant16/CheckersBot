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

``python3 main.py source/layouts/10x10.board``

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

``G3 F4``

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

``E5 C3 A1``

our piece will jump both of the bot's pieces and win the game.   

And that's all there really is to playing the game.  

## The Algorithm

This bot uses an iterative deepening depth-first search (IDDFS) with a minimax 
algorithm and Alpha-Beta pruning for decision making. The algorithm was inpsired by a 
[blog post](https://kartikkukreja.wordpress.com/2015/07/12/creating-a-bot-for-checkers/)
 from Kartik Kukreja. I've also included some links below if you're intersted 
in learning more about these algorithms.   

### Links

#### IDDFS

[The University of British Columbia](https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf)  
[Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)  
[The University of Nottingham](http://www.cs.nott.ac.uk/~pszbsl/G52APT/slides/09-Iterative-deepening.pdf)  
[artint.info](http://artint.info/html/ArtInt_62.html)  
[Blot post about uninformed searches by Kartik Kukreja](https://kartikkukreja.wordpress.com/2015/05/30/uninformed-search-algorithms/)  
[Part 1 of video by Prof. Douglas Fisher of Vanderbilt University](https://www.youtube.com/watch?v=7QcoJjSVT38)  
[Part 2 of video by Prof. Douglas Fisher of Vanderbilt University](https://www.youtube.com/watch?v=5MpT0EcOIyM)

#### Minimax and Alpha-Beta Pruning
[Wikipedia page for Minimax](https://en.wikipedia.org/wiki/Minimax)  
[Wikipedia page for Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)    
[Series of posts from geeksforgeeks.org](http://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)  
[University of California - Berkley lecture video about adversarial search](https://www.youtube.com/watch?feature=player_embedded&v=cwbjLIahbv8)  
[Supplemental Alpha-Beta pruning video by Prof Petier Abbeel of UC-Berkeley](https://www.youtube.com/watch?v=xBXHtz4Gbdo)  
[MIT Open Courseware Lecture on Minimax and Alpha-Beta](https://www.youtube.com/watch?v=STjW3eH0Cik)  
[Cornell University](https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/rec21.htm)
[Blog post about Alph-Beta pruning by Kartik Kukreja](https://kartikkukreja.wordpress.com/2014/06/29/alphabetasearch/)  
 
### Customizing the Algorithm
 If you open up main.py you'll see some constants at the top:

```
    SCORE
    DEPTH
    TIME
```

These constants are used by the bot to perform it's search algorithm.  

#### About these Variables

SCORE is the default score used by the minimax function. Changing it really 
won't benefit you because it is simply taking the place of infinity in the 
search algorithm.   

DEPTH is the max depth for the search algorithm. Changing this will change how 
many levels of the search tree that the IDDFS attempts to search.   

TIME is the max time to perform the search. There are approximately 
100,000,000,000,000,000,000 possible board states in a standard 8x8 game of 
checkers. Attempting to search them all would not be a wise task. Using 
Alpha-Beta pruning helps to reduce the branches of the tree we actually search,
but even with pruning the search can run a long time. By setting a time limit
 we are assured that the bot will choose a move in what we have decided is some
 reasonable amount of time.  

The bot also has a built in scoring function which it uses by default to assign
a score to the current state being looked at. It's a fairly naive algorithm 
which simply assigns a score to each piece on the board and returns the 
difference between the current player's score and the other player's score.  

```python3
    def pieces_count(state):
        bot, player = 0, 0
        for row in state.board:
            for square in row:
                if square == 'b':
                    bot += 1.0
                elif square == 'B':
                    bot += 1.5
                elif square == 'p':
                    player += 1.0
                elif square == 'P':
                    player += 1.5
        return (bot - player) if state.bots_move else (player - bot)
```

There are definitely better, more complex heuristics that could be used and 
you're welcome to create your own scoring function for use by the bot. To do 
so simply implement your new scoring algorithm where noted in the file and then 
pass it in when creating the new CheckersGame object to override the default 
argument.  

For example, if I created a new scoring function called 'best_ever', I would 
change the calls to the CheckersGame constructors like so:

``game = CheckersGame(sys.argv[1], SCORE, DEPTH, TIME, bot_func=best_ever)``

``game = CheckersGame('source/layouts/8x8.board', SCORE, DEPTH, TIME, bot_func=best_ever)``

This would cause the game to use your custom scoring function. 

