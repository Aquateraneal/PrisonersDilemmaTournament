import random
import numpy as np

# Investigator strategy
# Every 24 turns, goes through the eight possible trios of moves.
# The best strat from the previous go-through gets boosted by 1,
# and the worst gets removed.
#
# By Aquateraneal

moves = [[False, False, False],
         [False, False, True ],
         [False, True , False],
         [False, True , True ],
         [True , False, False],
         [True , False, True ],
         [True , True , False],
         [True , True , True ]]
scores = [0] * 8

def my_score(history: list[list[bool]]):
    score = 0
    for x in zip(history):
        score += [1, 0, 5, 3][x[0] + 2*x[1]] # type: ignore
    return score

def strategy(history, memory):
    gamelen = history.shape[1]
    if gamelen and not gamelen % 3:
        'calc scores'
    if gamelen and not gamelen % 24:
        'change `moves`'
    return sum(moves, [])[gamelen % 24]
