class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])

        map = defaultdict(list)

        for row in range(ROWS):
            for col in range(COLS):
                map[row-col].append(mat[row][col])
        
        for values in map:
            map[values].sort(reverse = True)
        
        for row in range(ROWS):
            for col in range(COLS):
                mat[row][col] = map[row-col].pop()
        return mat


        