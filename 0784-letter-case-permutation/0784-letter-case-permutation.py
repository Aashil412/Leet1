class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = []
        solution = []

        def dfs(index):
            if index >= len(s):
                results.append(''.join(solution[:]))
                return
            
            if s[index].isalpha():
                #lowercase
                solution.append(s[index].lower())
                dfs(index+1)
                solution.pop()

                #uppercase
                solution.append(s[index].upper())
                dfs(index+1)
                solution.pop()
            
            else:
                solution.append(s[index])
                dfs(index+1)
                solution.pop()
        dfs(0)
        return results
        