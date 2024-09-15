class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results, current = [], [] 

        def dfs(index, current_sum):
            if current_sum == target:
                results.append(current[:])
                return
            if index >= len(candidates) or current_sum > target:
                return 
            current.append(candidates[index])
            dfs(index, current_sum + candidates[index])
            current.pop()
            dfs(index + 1, current_sum)
        dfs(0, 0)
        return results