class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        while matrix:
            # Check Top
            results.extend(matrix.pop(0))

            #check right side
            if matrix and matrix[0]:
                for row in matrix:
                    results.append(row.pop())

            # check bottom side
            if matrix:
                results.extend(matrix.pop()[::-1])

            #check left side
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    results.append(row.pop(0))
        return results




        