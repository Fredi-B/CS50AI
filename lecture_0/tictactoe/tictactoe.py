"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def main():
    print(actions([[X, O, X],
            [EMPTY, X, O],
            [EMPTY, EMPTY, EMPTY]]))


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    cnt_X = 0
    cnt_O = 0
    for row in board:
        for player in row:
            if player is X:
                cnt_X += 1
            if player is O:
                cnt_O += 1
    return X if cnt_X <= cnt_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell is EMPTY:
                actions_set.add((i, j))
            j += 1
        i += 1
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()