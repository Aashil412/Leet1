class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #row[i] = col[i]
        ROWS = len(matrix)
        COLS = len(matrix[0])
        transpose = []
        for col in range(COLS):
            temp = []
            for row in range(ROWS):
                temp.append(matrix[row][col])
            transpose.append(temp)
        return transpose