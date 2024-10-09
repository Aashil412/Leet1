class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # add the number at the index
        #[2,3,1] [2,1,3] [1,2,3]
        results = []
        solution = []

        def dfs():
            if len(solution) == len(nums):
                results.append(solution[:])
                return 
            for num in nums:
                if num in solution:
                    continue
                else:
                    solution.append(num)
                    dfs()
                    solution.pop()
        dfs()
        return results
        """
        Input: nums = [0,1]
        Output: [[0,1],[1,0]]
        """