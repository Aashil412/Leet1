class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        happy_array = ['a','b','c']

        results = []
        self.k = k
        def backtracking(solution):
            if len(solution) == n:
                self.k -= 1
                if self.k == 0:
                    results.append(''.join(solution))
                return

            for char in happy_array:
                if not solution or solution[-1] != char:
                    solution.append(char)
                    backtracking(solution)
                    solution.pop()
                    if results:
                        return
        
        backtracking([])
        return results[0] if results else ""