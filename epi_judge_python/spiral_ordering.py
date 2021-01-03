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

test_square3 = [[1,2,3],[4,5,6],[7,8,9]]

def annotated_epi_solution1(square_matrix: List[List[int]]) -> List[int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # square_matrix has odd dimension, and we are at the center of the
            # matrix square_matrix.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        ## pythonic list iteration syntax. smart
        ## start from offset, go up to and including last element - offset
        spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
        ## smart. changes rows into column. therefore
        ## -1 - offset is getting at the right most column of the square
        ## list(zip(*test_square3)) = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(square_matrix[-1 - offset][-1 -
                                                          offset:offset:-1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset:offset:-1])

    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        ## 3 square, iterate over [0,1]. 1 is center.
        ## 4 square, iterate over [0,1]. 1 is just next square
        matrix_layer_in_clockwise(offset)
    return spiral_ordering

def epi_smart_solution(square_matrix: List[List[int]]) -> List[int]:
    square_length = len(square_matrix)
    direction = row = col = 0
    shift = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    spiral: List[int] = []
    for _ in range(square_length ** 2):
        spiral.append(square_matrix[row][col])
        square_matrix[row][col] = 0
        next_row, next_col = row + shift[direction][0], col + shift[direction][1]
        if ((next_row not in range(0, square_length))
                or (next_col not in range(0, square_length))
                or (square_matrix[next_row][next_col] == 0)
                ):
            direction = (direction + 1) & 3 ## the smart epi way to do x mod 4
            next_row, next_col = row + shift[direction][0], col + shift[direction][1]

        row, col = next_row, next_col

    return spiral

if __name__ == '__main__':
    generic_test.generic_test_main('spiral_ordering.py',
                                    'spiral_ordering.tsv',
                                    matrix_in_spiral_order)
    print('epi smart solution')
    generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       epi_smart_solution)
