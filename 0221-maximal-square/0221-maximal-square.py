class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}

        def dfs(row, col):
            if row >= ROWS or col >= COLS:
                return 0
            if (row, col) not in cache:

                down = dfs(row + 1, col)
                right = dfs(row, col + 1)
                diagonal = dfs(row + 1, col + 1)

                cache[(row,col)] = 0
                if matrix[row][col] == "1":
                    cache[(row, col)] = 1 + min(down, right, diagonal)
 
            return cache[(row,col)]
        dfs(0,0)
        return max(cache.values()) ** 2
