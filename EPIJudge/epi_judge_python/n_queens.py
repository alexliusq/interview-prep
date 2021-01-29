from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    def row_placement(row):
        if row == n:
            result.append(list(column_placements))
            return
        available_cols = set(range(n))
        for prev_row in range(row):
            prev_col = column_placements[prev_row]
            diff = row - prev_row
            remove_cols = set([prev_col, prev_col - diff, prev_col + diff])
            available_cols -= remove_cols
        for col in available_cols:
            column_placements[row] = col
            row_placement(row + 1)

    result = []
    column_placements = [0] * n
    row_placement(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
