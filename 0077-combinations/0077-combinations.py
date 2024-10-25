class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        solution = []

        def dfs(start):
            if len(solution) == k:
                results.append(solution[:])
                return
            
            for i in range(start, n + 1): 
                solution.append(i)
                dfs(i + 1)
                solution.pop()

        dfs(1)
        return results