from typing import List, NamedTuple

from test_framework import generic_test

from collections import deque, namedtuple

Coordinate = namedtuple('coordinate', ('x', 'y'))

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:

    original = image[x][y]
    queue = deque([Coordinate(x, y)])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        current = queue.popleft()
        image[current.x][current.y] = not original
        for direction in directions:
            possible_coordinate = Coordinate(current.x + direction[0], current.y + direction[1])
            if (0 <= possible_coordinate.x < len(image) and
                0 <= possible_coordinate.y < len(image[0]) and
                image[possible_coordinate.x][possible_coordinate.y] == original
            ):
                queue.append(possible_coordinate)
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
