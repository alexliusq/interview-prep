from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def min_path(row, col):
            if row == 0 and col == 0:
                return grid[row][col]
            if row > 0 and col > 0:
                return min(min_path(row -1, col), min_path(row, col - 1)) + grid[row][col]
            if row == 0:
                return min_path(row, col - 1) + grid[row][col]
            if col == 0:
                return min_path(row - 1, col) + grid[row][col]
        
        return min_path(len(grid) - 1, len(grid[0]) - 1)