from os import sched_yield
from typing import List

from test_framework import generic_test
from collections import namedtuple, deque

def fill_surrounded_regions(board: List[List[str]]) -> None:
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    reachable_squares = set()
    for x_edge in [0, len(board) - 1]:
        for y_iter in range(len(board[0])):
            if board[x_edge][y_iter] == 'W':
                reachable_squares.add(Coordinate(x_edge,y_iter))
    for y_edge in [0, len(board[0]) -1]:
        for x_iter in range(len(board)):
            if board[x_iter][y_edge] == 'W':
                reachable_squares.add(Coordinate(x_iter, y_edge))

    queue = deque(reachable_squares)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        (x,y) = queue.popleft()
        for direction in directions:
            candidate = Coordinate(x + direction[0], y + direction[1])
            if candidate in reachable_squares:
                continue
            if (0 <= candidate.x < len(board) and
                0 <= candidate.y < len(board[0]) and
                board[candidate.x][candidate.y] == 'W'
            ):
                reachable_squares.add(candidate)
                queue.append(candidate)
                
    for x in range(len(board)):
        for y in range(len(board[0])):
            if Coordinate(x,y) not in reachable_squares:
                board[x][y] = 'B'
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
