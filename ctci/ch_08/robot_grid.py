
def find_path(grid):
    def dfs(row, col):
        print(row, col)
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            return True
        
        if row == len(grid):
            return False
        
        if col == len(grid[0]):
            return False
        
        if not grid[row][col]:
            return False
        
        grid[row][col] = False
        for next_row, next_col in [[row + 1, col], [row, col + 1]]:
            if dfs(next_row, next_col):
                return True
        
        return False

    return dfs(0, 0)

test = [
    [True, True, False],
    [False, True, False],
    [False, True, True]
]

print(find_path(test))