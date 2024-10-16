class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find which row is the target is on by checking if its less or greater
        ROWS = len(matrix)
        COLS = len(matrix[0])
        left = 0
        right = ROWS * COLS - 1
        # 11 // 2 = 5
        # 5 // 4 = 1
        # 5 % 4 = 1
        while left <= right:
            middle = (right + left) // 2
            middle_value = matrix[middle // COLS][middle % COLS]

            if middle_value == target:
                return True
            elif middle_value < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
