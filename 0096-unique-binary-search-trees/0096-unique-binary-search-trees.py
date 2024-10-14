class Solution:
    def numTrees(self, n: int) -> int:
        cache = [1] * (n + 1)
        # 5
        # 1, 2, 3, 4, 5
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                leftNode = root - 1
                rightNode = nodes - root
                total += cache[leftNode] * cache[rightNode]
            cache[nodes] = total
        return cache[n] 