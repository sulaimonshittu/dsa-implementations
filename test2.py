def orangesRotting(grid):
    def dfs(row, col, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        count = 0
        for r, c in directions:
            new_row, new_col = row + r, col + c
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                grid[new_row][new_col] = 2
                count += 1
        return count

    rows, cols = len(grid), len(grid[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                if dfs(row, col, grid) > 0:
                    count += 1
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                return -1
    return count

orangesRotting([[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]])