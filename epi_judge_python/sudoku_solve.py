import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def get_next_index(partial_assignment):
        for i in range(len(partial_assignment)):
            for j in range(len(partial_assignment)):
                if partial_assignment[i][j] == 0:
                    return (i,j)
        return None

    next_index = get_next_index(partial_assignment)
    
    if next_index is None:
        return True
    valid_values = set(range(1,10))
    row, col = next_index
    for num in partial_assignment[row]:
        valid_values.discard(num)
    for num in list(zip(*partial_assignment))[col]:
        valid_values.discard(num)
    block_num = (row // 3) + (col // 3) * 3
    block = gather_square_block(partial_assignment, 3, block_num)
    # print('block', block)
    for num in block:
        valid_values.discard(num)
    # print('valid values', valid_values)
    for num in valid_values:
        # print('trying for index', next_index, 'value', num)
        partial_assignment[row][col] = num
        if solve_sudoku(partial_assignment):
            return True
        else:
            partial_assignment[row][col] = 0
    return False


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))
    # print(solved)
    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
