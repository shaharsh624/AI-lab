import numpy as np


def heuristic(matrix, goal_matrix):
    x = matrix == goal_matrix
    return 9 - np.count_nonzero(x)


def possibleChildren(matrix):
    visited.add()


visited = []
open = []
closed = []

start_matrix = [[2, 8, 3][1, 6, 4][7, 0, 5]]
goal_matrix = [[1, 2, 3][8, 0, 4][7, 6, 5]]
