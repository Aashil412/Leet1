class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        row_list = [0] * ROWS
        col_list = [0] * COLS

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    row_list[row] += 1
                    col_list[col] += 1

        count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row_list[row] > 1 or col_list[col] > 1):
                    count += 1
        return count
        