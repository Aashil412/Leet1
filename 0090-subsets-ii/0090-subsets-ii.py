class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_set = set()
        nums_size = len(nums)
        solution = []
        results = []
        nums.sort()
        def dfs(i):
            if i >= nums_size:
                if tuple(solution[:]) not in num_set:
                    results.append(solution[:])
                    num_set.add(tuple(solution[:]))
                return
            
            solution.append(nums[i])
            dfs(i+1)
            solution.pop()
            dfs(i+1)
        dfs(0)
        return results