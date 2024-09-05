"""
Tic Tac Toe Player
"""

import math
import copy


X = "X"
O = "O"
EMPTY = None


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
    new_board = copy.deepcopy(board)
    i, j = action
    if i < 0 or j < 0:
        raise IndexError
    if new_board[i][j] == EMPTY:
        new_board[i][j] = player(board)
    else:
        raise ValueError
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    check_functions = [check_columns, check_rows, check_diagonals]
    for check in check_functions:
        ret_val = check(board)
        if ret_val is not None:
            return ret_val
    return None


def check_rows(board):
    for row in board:
        for i in range(len(row) - 1):
            if row[i] is EMPTY or row[i] != row[i + 1]:
                break
            if i == 1:
                return row[0]
    return None


def check_columns(board):
    len_cols = len(board[0])
    len_rows = len(board)
    for i in range(len_cols):
        for j in range(len_rows - 1):
            if board[j][i] is EMPTY or board[j][i] != board[j + 1][i]:
                break
            if j == 1:
                return board[0][i]
    return None


def check_diagonals(board):
    if board[0][0] is not EMPTY:
        if len(set([board[0][0], board[1][1], board[2][2]])) == 1:
            return board[0][0]
    if board[2][0] is not EMPTY:
        if len(set([board[2][0], board[1][1], board[0][2]])) == 1:
            return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_val = winner(board)
    return 1 if winner_val == X else -1 if winner_val == O else 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    return action


def max_value(board):
    '''
    Recursive function.
    Returns the value and the optimal action of a board.
    '''

    # Return value of terminal board
    if terminal(board):
        return utility(board), None
    
    # Initial value set to -infinity
    v = float('-inf')

    # Loop through all possible actions
    actions_set = actions(board)
    for action in actions_set:
        v_tmp,_ = min_value(result(board, action))

        # Store the best action
        if v_tmp > v:
            optimal_action = action
            v = v_tmp

    return v, optimal_action


def min_value(board):
    '''
    Recursive function.
    Returns the value and the optimal action of a board.
    '''

    # Return value of terminal board
    if terminal(board):
        return utility(board), None

    # Initial value set to infinity
    v = float('inf')

    # Loop through all possible actions
    actions_set = actions(board)
    for action in actions_set:
        v_tmp,_ = max_value(result(board, action))

        # Store the best action
        if v_tmp < v:
            optimal_action = action
            v = v_tmp

    return v, optimal_action
