from typing import List

from test_framework import generic_test
import functools

def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:

    @functools.cache
    def find_adjacent(coordinate, token):
        result = []
        for direction in directions:
            adjacent = (coordinate[0] + direction[0], coordinate[1] + direction[1])
            if  adjacent[0] < 0 or adjacent[0] >= len(grid):
                continue
            if adjacent[1] < 0 or adjacent[1] >= len(grid[0]):
                continue
            # if adjacent in prefix:
            #     continue
            # print(token, adjacent, grid[adjacent[0]][adjacent[1]])
            if (grid[adjacent[0]][adjacent[1]] == token):
                result.append(adjacent)
        return result

    def search_for_token(pattern_index):
        token = pattern[pattern_index]

        if pattern_index == 0:
            return [(i, j)
            for i in range(len(grid))
                for j in range(len(grid[i]))
                    if token == grid[i][j]
            ]

        prefixes = search_for_token(pattern_index - 1)
        # print(prefixes)
        result = set()
        for tail in prefixes:
            # tail = prefix[-1]
            adjacent = find_adjacent(tail, token)
            result.update(adjacent)
        # print(token, result)
        return result

    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    result = search_for_token(len(pattern) - 1)
    # print(result)
    return len(result) > 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
