from typing import List

from test_framework import generic_test

def is_valid_subset(subset: List[int]) -> bool:
    check_array = [False for x in range(10)] ## just for easier indexing. 
    for element in subset:
        if element == 0:
            continue ## CONTINUE, not break
        if check_array[element]:
            print(subset)
            return False
        check_array[element] = True
    return True

## want to get 3x3 grids starting from
## (0,0) (0,3) (0,6)
## (3, 0) (3,3)...
def get_all_subgrids(grid: List[List[int]]) -> List[List[int]]:
    subgrid_list = []
    for row_start in [ 3 * x for x in range(3)]:
        for col_start in [ 3 * x for x in range(3)]:
            subgrid_list.append([
                grid[row][col] for row in range(row_start, row_start + 3)
                    for col in range(col_start, col_start + 3)
            ])
    return subgrid_list

# brute force
# visit each square 3 times
def brute_force(partial_assignment: List[List[int]]) -> bool:
    for row in partial_assignment:
        if (not is_valid_subset(row)): return False
    for col in list(zip(*partial_assignment)):
        if (not is_valid_subset(col)): return False
    for subgrid in get_all_subgrids(partial_assignment):
        if (not is_valid_subset(subgrid)): return False
    return True

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    return True


if __name__ == '__main__':
    generic_test.generic_test_main('is_valid_sudoku.py',
                                    'is_valid_sudoku.tsv', brute_force)
