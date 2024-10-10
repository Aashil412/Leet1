class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        results = []
        while left <= right and top <= bottom:
            #top
            for i in range(left, right + 1):
                results.append(matrix[top][i])
            #right
            for i in range(top + 1, bottom + 1):
                results.append(matrix[i][right])
            #bottom
            if bottom != top:
                for i in range(right - 1, left - 1, -1):
                    results.append(matrix[bottom][i])
            #left
            if left != right:
                for i in range(bottom - 1, top, -1):
                    results.append(matrix[i][left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1
        return results
