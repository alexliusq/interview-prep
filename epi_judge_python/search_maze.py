import collections
import copy
from decimal import ROUND_05UP
import functools
from os import stat_result
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    visited = set()
    directions = [(-1,0), (1,0), (0,1), (0, -1)]
    def search_coordinate(current: Coordinate) -> List[Coordinate]:
        if current == e:
            return [e]
        if current in visited:
            return []
        visited.add(current)
        # print('yolo')
        for direction in directions:
            next_coordinate = Coordinate(current[0] + direction[0], current[1] + direction[1])
            # print(next_coordinate)
            if (0 <= next_coordinate[0] < len(maze) and
                0 <= next_coordinate[1] < len(maze[0]) and
                maze[next_coordinate[0]][next_coordinate[1]] == WHITE
                ):
                possible_path = search_coordinate(next_coordinate)
                if possible_path:
                    possible_path.append(current)
                    return possible_path
        return []
    # print(maze)
    path_to_end = search_coordinate(s)
    path_to_end.reverse()
    # print(path_to_end)
    return path_to_end


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
