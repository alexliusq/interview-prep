from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    side_length = len(square_matrix)
    square_count = 0
    spiral = []
    while side_length > 1:
        row, col = square_count, square_count
        visit_count = side_length - 1
        for i in range(visit_count):
            spiral.append(square_matrix[row][col])
            col += 1
        for i in range(visit_count):
            spiral.append(square_matrix[row][col])
            row += 1
        for i in range(visit_count):
            spiral.append(square_matrix[row][col])
            col -= 1
        for i in range(visit_count):
            spiral.append(square_matrix[row][col])
            row -= 1
        square_count += 1
        side_length -= 2
    if side_length == 1:
        spiral.append(square_matrix[square_count][square_count])
    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
