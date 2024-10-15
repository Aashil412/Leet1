class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        numLen = len(nums)
        for i in range(numLen):
            for j in range(numLen):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count

        