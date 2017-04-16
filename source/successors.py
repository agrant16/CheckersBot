#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""successors

File: successors.py\n
Author: Alan Grant\n
Version: 1.0\n
Date: 04/12/2017\n
Class: CSCI-C 458\n

This module provides access to the Successor Generator class. This class is
used by the checkers simulation for a checkers playing robot.
"""


from copy import deepcopy
from .checkers_state import CheckersState


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

    def _get_steps(self, piece):
        """_get_steps
        The _get_steps method returns the directions a piece can move as a
        list of tuples.

        Args:
            piece (str) : The piece for the current move.

        Returns:
            list : A list of tuples representing the directions piece can move.
        """
        steps = []
        if piece != 'b':
            steps += [(-1, -1), (-1, 1)]
        if piece != 'p':
            steps += [(1, -1), (1, 1)]
        return steps

    def _king_condition(self, x):
        """ _king_condition

        The _king_condition method checks if a king condition has been met for
        either player. This is when a piece from either player has reached the
        far row of the board.

        Args:
            x (int) : The row number of the end point of the current move.

        Returns:
            bool : True if a king condition has been met, False otherwise.
        """
        return ((x == (self.state.size - 1) and self.state.bots_move)
                or (x == 0 and not self.state.bots_move))

    def _in_bounds(self, x, y):
        """_in_bounds

        The _in_bounds method checks board[x][y] is a square on the board.

        Args:
            x (int) : The x coordinate of the piece.\n
            y (int) : The y coordinate of the piece.

        Returns:
            bool : True if the piece is in bounds, False otherwise.
        """
        x_in = x >= 0 and x < self.state.size
        y_in = y >= 0 and y < self.state.size
        return x_in and y_in

    def _is_empty(self, board, x, y):
        """_is_empty

        The _is_empty method checks to see if board[x][y] is an empty square.

        Args:
            x (int) : The x coordinate of the square.\n
            y (int) : The y coordinate of the square.

        Returns:
            bool : True if the square is empty, False otherwise.
        """
        return board[x][y] == '_'

    def _same_color(self, board, x, y, x2, y2):
        """_same_color

        The _same_color method checks to see if the pieces at board[x][y] and
        board[x2][y2] are the color.

        Args:
            x (int) : The row of the jumper.\n
            y (int) : The column of the jumper.\n
            x2 (int) : The row of the jumped piece.\n
            y2 (int) : The column of the jumped piece.\n

        Returns:
            bool : True if the pieces are the same color, False otherwise.
        """
        return board[x][y].lower() == board[x2][y2].lower()

    def _can_land(self, board, x, y):
        """_can_land

        The _can_land method checks to see if board[x][y] is a spot where a
        piece can legally land upon finishing a move.

        Args:
            x (int) : The row of the landing spot.\n
            y (int) : The column of the landing spot.

        Returns:
            bool : True if the spot is an empty square on the board,
            False otherwise.
        """
        return self._in_bounds(x, y) and self._is_empty(board, x, y)

    def _gen_moves(self, x, y, successors):
        """_gen_moves

        The _gen_moves method generates CheckersStates representing the ending
        state of all legal normal moves a the piece at board[x][y] can make.
        It returns these moves as a list of CheckerStates objects.

        Args:
            x (int) : The current row number of the piece's location.
            y (int) : The current column number of the piece's location.
            successors (list) : A list of possible ending CheckersStates.
        """
        for step in self._get_steps(self.state.board[x][y]):
            x2, y2 = x + step[0], y + step[1]  # The end point

            """Check if it is legal to move to the end point:
                i.e. the end point is in bounds and not
                occupied."""
            if self._can_land(self.state.board, x2, y2):
                # Copy board and update copy with new move.
                board_copy = deepcopy(self.state.board)
                board_copy[x2][y2] = board_copy[x][y]
                board_copy[x][y] = '_'

                # King the piece if it has reached the far row.
                if self._king_condition(x2):
                    board_copy[x2][y2] = board_copy[x2][y2].upper()

                # Create new CheckersState and append to successors.
                successors.append(CheckersState(
                                  board_copy, not self.state.bots_move,
                                  [(x, y), (x2, y2)], self.state.size))

    def _can_jump(self, board, x, y, x2, y2):
        """_can_jump

        The _can_jump method checks to see if the piece located at
        board[x2][y2] can be jumped by the piece at board[x][y].

        Args:
            x (int) : The row of the jumper.\n
            y (int) : The column of the jumper.\n
            x2 (int) : The row of the jumped piece.\n
            y2 (int) : The column of the jumped piece.\n

        Returns:
            bool : True if the piece at board[x][y] can be jumped by the piece
            at board[i][j], False otherwise.
        """
        if self._in_bounds(x2, y2):
            return (not self._is_empty(board, x2, y2) and not
                    self._same_color(board, x, y, x2, y2))

    def _gen_jumps(self, board, x, y, moves, successors):
        """_gen_jumps

        The _gen_jumps method generates CheckersStates representing the ending
        state of all legal jumps a piece can make. It adds these CheckersStates
        to successors.

        Args:
            i (int) : The current row number of the piece's location.\n
            j (int) : The current column number of the piece's location.\n
            moves (list) : A list of tuples (x,y) representing the sequence of
            steps in the jump move.\n
            successors (list) : A list of possible ending CheckersStates.
        """
        end_jump = True
        for step in self._get_steps(board[x][y]):
            # The loc of the square to be jumped.
            x2, y2 = x + step[0], y + step[1]

            """Check if the square can be jumped
                    i.e the the square is in bounds, not empty,
                    and it holds a piece of the opposite color."""
            if self._can_jump(board, x, y, x2, y2):
                x3, y3 = x2 + step[0], y2 + step[1]  # The landing point

                if self._can_land(board, x3, y3):
                    # Update the board and store previous squares
                    board[x3][y3] = board[x][y]
                    save = board[x2][y2]
                    board[x][y] = board[x2][y2] = '_'
                    previous = board[x3][y3]

                    # King the piece if it has reached the far row.
                    if self._king_condition(x3):
                        board[x3][y3] = board[x3][y3].upper()

                    moves.append((x3, y3))

                    # Check if more jumps can be made.
                    self._gen_jumps(board, x3, y3, moves, successors)

                    # Adjust the moves list and board when no more jumps are
                    # possible.
                    moves.pop()
                    board[x][y] = previous
                    board[x2][y2] = save
                    board[x3][y3] = '_'
                    end_jump = False

        if end_jump and len(moves) > 1:
            successors.append(CheckersState(deepcopy(board),
                              not self.state.bots_move, deepcopy(moves),
                              self.state.size))

    def _generate(self, successors, player, gen_func, jumps=False):
        """_generate

        The _geneate method is a helper functon used to call the methods
        _gen_moves and _gen_jumps.

        Args:
            successors (list) : List of CheckersState objects represent all
            valid successors of the current state.\n
            player (str) : A character repesenting the current player piece.\n
            gen_func (function) : The name of the gen function to use.\n
            jumps (bool) : True if gen_jumps is to be used, False otherwise.
            Defaults to False.
        """
        for x in range(self.state.size):
            for y in range(self.state.size):
                if self.state.board[x][y].lower() == player:
                    if not jumps:
                        gen_func(x, y, successors)
                    else:
                        gen_func(self.state.board, x, y, [(x, y)], successors)
        return successors

    def update_state(self, new_state):
        """update_state

        The update_state function does exactly what it says i does: updates
        the current state to a new state.

        Args:
            new_state (CheckersState) : The most recent state of the game.
        """
        self.state = new_state

    def successors(self):
        """successors

        The successors method generates all possible successors of the
        current CheckersState and returns them as a list of CheckersState
        objects.

        Returns:
            successors (list) : A list of CheckersState objects representing
            the possible successor states.
        """
        player = 'b' if self.state.bots_move else 'p'
        successors = self._generate([], player, self._gen_jumps, True)
        successors += self._generate([], player, self._gen_moves)
        return successors
