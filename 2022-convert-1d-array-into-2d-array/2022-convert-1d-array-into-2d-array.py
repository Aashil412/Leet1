class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        array_2D = [[0] * n for _ in range(m)]

        for i in range(len(original)):
            array_2D[i // n][i % n] = original[i]
        return array_2D

        