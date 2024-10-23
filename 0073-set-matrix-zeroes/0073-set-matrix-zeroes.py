class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        row_set = set()
        col_set = set()

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        # 1
        # 1
        for row in row_set:
            for col in range(COLS):
                matrix[row][col] = 0

        for col in col_set:
            for row in range(ROWS):
                matrix[row][col] = 0
        return matrix