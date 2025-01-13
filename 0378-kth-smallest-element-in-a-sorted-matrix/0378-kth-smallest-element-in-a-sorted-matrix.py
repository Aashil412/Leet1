class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
            size = len(matrix)
            left, right = matrix[0][0], matrix[size-1][size-1]

            def good(num):
                column = size - 1
                count = 0
                for row in range(size):
                    while column >= 0 and num < matrix[row][column]:
                        column -= 1
                    count += column + 1
                return count

            while left < right:
                middle = left + (right - left) // 2
                if good(middle) < k:
                    left = middle + 1
                else:
                    right = middle 

            return left