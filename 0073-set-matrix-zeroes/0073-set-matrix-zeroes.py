class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])

        row_set = set()
        col_set = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        for i in row_set:
            for col in range(COLS):
                matrix[i][col] = 0
        for j in col_set:
            for row in range(ROWS):
                matrix[row][j] = 0

        return matrix 

        