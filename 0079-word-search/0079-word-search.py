class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col, index):

            if index == len(word):
                return True

            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[index] and (row,col) not in visited:
                visited.add((row,col))

                results = (dfs(row - 1, col, index + 1) or
                dfs(row + 1, col, index + 1) or
                dfs(row, col - 1, index + 1) or
                dfs(row, col + 1, index + 1)) 

                visited.remove((row,col))

                return results

            return False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    visited = set()
                    if dfs(row, col, 0):
                        return True

        return False