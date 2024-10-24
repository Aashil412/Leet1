class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0]) 

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] != word[index]:
                return False
        
            directions = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            temp = board[row][col]
            board[row][col] = '#'

            for r, c in directions:
                if dfs(r, c, index + 1):
                    return True
            board[row][col] = temp
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
        
