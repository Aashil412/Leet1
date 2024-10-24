class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        solution = []
        
        def dfs(index):
            if index == len(nums):
                results.append(solution[:])
                return
            
            solution.append(nums[index])
            dfs(index + 1)
            solution.pop()
            dfs(index + 1)
            
        dfs(0)
        return results