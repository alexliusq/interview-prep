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

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                elif row == 0 and col > 0:
                    grid[row][col] += grid[row][col - 1]
                elif col == 0 and row > 0:
                    grid[row][col] += grid[row - 1][col]
                else: ## row > 0 and col > 0
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
        # print(grid)
        return grid[-1][-1]