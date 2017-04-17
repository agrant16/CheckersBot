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
algorithm and alpha-beta pruning for decision making. The algorithm was inpsired by a 
[blog post](https://kartikkukreja.wordpress.com/2015/07/12/creating-a-bot-for-checkers/)
 from Kartik Kukreja. I've also included some links below if you're intersted 
in learning more about these algorithms.   

### Links

#### IDDFS

* [The University of British Columbia](https://www.cs.ubc.ca/~hutter/teaching/cpsc322/2-Search6-final.pdf)
* [Wikipedia](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
* [The University of Nottingham](http://www.cs.nott.ac.uk/~pszbsl/G52APT/slides/09-Iterative-deepening.pdf)
* [artint.info](http://artint.info/html/ArtInt_62.html)
* [Blog post about uninformed searches by Kartik Kukreja](https://kartikkukreja.wordpress.com/2015/05/30/uninformed-search-algorithms/)
* [Part 1 of video by Prof. Douglas Fisher of Vanderbilt University](https://www.youtube.com/watch?v=7QcoJjSVT38)
* [Part 2 of video by Prof. Douglas Fisher of Vanderbilt University](https://www.youtube.com/watch?v=5MpT0EcOIyM)

#### Minimax and Alpha-Beta Pruning
* [Wikipedia page for minimax](https://en.wikipedia.org/wiki/Minimax)
* [Wikipedia page for alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
* [Series of posts from geeksforgeeks.org](http://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
* [University of California - Berkley lecture video about adversarial search](https://www.youtube.com/watch?feature=player_embedded&v=cwbjLIahbv8)
* [Supplemental alpha-beta pruning video by Prof Petier Abbeel of UC-Berkeley](https://www.youtube.com/watch?v=xBXHtz4Gbdo)
* [MIT 6.034 OCW lecture video on minimax and alpha-beta featuring Prof. Patrick Winston](https://www.youtube.com/watch?v=STjW3eH0Cik)
* [MIT 6.034 OCW recitation on minimax and alpha-beta featuring Mark Seifter](https://www.youtube.com/watch?v=hM2EAvMkhtk)
* [Cornell University page on minimax and alpha-beta](https://www.cs.cornell.edu/courses/cs312/2002sp/lectures/rec21.htm)
* [Blog post about Alph-Beta pruning by Kartik Kukreja](https://kartikkukreja.wordpress.com/2014/06/29/alphabetasearch/)
 
### Customizing the Algorithm
If you open up main.py you'll see some constants at the top. These constants 
are used by the bot to perform it's search algorithm.

* SCORE
  * This is the default score used by the minimax function. Changing it really 
won't benefit you because it is simply taking the place of infinity in the 
search algorithm. 

* DEPTH
  * The max depth for the search algorithm. Changing this will change how 
many levels of the search tree that the IDDFS attempts to search.

* TIME
  * The max time to perform the search. There are approximately 
100,000,000,000,000,000,000 possible board states in a standard 8x8 game of 
checkers. Attempting to search them all would not be a wise task. Using 
Alpha-Beta pruning helps to reduce the branches of the tree we actually search,
but even with pruning the search can run a long time. By setting a time limit
 we are assured that the bot will choose a move in what we have decided is some
 reasonable amount of time.

The bot also has a built in scoring function which it uses by default to assign
a score to the current state being looked at. It's a fairly naive algorithm 
which does three things: it assigns a score to each piece on the board,sums the
scores for each player, and returns the difference between the current player's 
score and the other player's score.

Each piece's score is determined by three factors: 

* Is it kinged?
  * Kings have a base value of 2 points. 
  * Normal pieces have a base value of 1 point.

* If not how close is it to the far side of the board and being kinged?
  * If a piece is normal its score is multiplied by a modifier based on how many 
squares, in a straight line, it is from being kinged. So if we're playing on a 
standard 8x8 checkers board and a piece is 2 squares away from being kinged 
then that piece will have its total score multiplied by (1 + 6/8) or 1.75.

* Is it invulnerable?

  * If a piece is in a corner, or against an edge, it is impossible for the 
opponenet to capture that piece. Pieces in these positions have their base 
value increased by 1. So a king in this situation is worth 3 points and a 
normal piece in this situation is worth 2 points.

```python
def _is_invulnerable(state, x, y):
    x_bounds = x == 0 or x == (state.size - 1)
    y_bounds = y == 0 or y == (state.size - 1)
    return x_bounds or y_bounds

def _score(state):
    bot, player = 0, 0
    for x, row in enumerate(state.board):
        for y, square in enumerate(row):
            if _is_invulnerable(state, x, y):
                adjuster = 1 
            else:
                adjuster = 0

            if square == 'b':
                bot += (1.0 + adjuster) * (1 + (.1 * ((x + 1) / state.size)))
            elif square == 'B':
                bot += 2.0 + adjuster
            elif square == 'p':
                player += (1.0 + adjuster) * (1 + (.1 * ((state.size - x) 
                                             / state.size)))
            elif square == 'P':
                player += 2.0 + adjuster

    return (bot - player) if state.bots_move else (player - bot)
```

There are definitely better, more complex heuristics that could be used and 
you're welcome to create your own scoring function for use by the bot. To do 
so simply implement your new scoring algorithm where noted in main.py and then 
pass it in when creating the new CheckersGame object to override the default 
argument.  

For example, if I created a new scoring function called "best_ever", I would 
change the calls to the CheckersGame constructors like so:

```python
if len(sys.argv) > 1:
    game = CheckersGame(sys.argv[1], SCORE, DEPTH, TIME, bot_func=best_ever)
else:
    game = CheckersGame('layouts/8x8.board', SCORE, DEPTH, TIME, bot_func=best_ever)
```

This would cause the game to use your custom scoring function. 
