class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        # 0  1 2
        # 1  2 3
        # 2  3 4
        results = []
        diagonals = {}
        for row in range(ROWS):
            for col in range(COLS):
                if row + col not in diagonals:
                    diagonals[row+col] = []
                diagonals[row+col].append(mat[row][col])
        
        for diags in range(len(diagonals)):
            if diags % 2 == 0:
                results.extend(diagonals[diags][::-1])
            else:
                results.extend(diagonals[diags])
        return results