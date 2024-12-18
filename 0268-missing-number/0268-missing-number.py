class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        count = 1
        for i in range(len(nums)):
            num += count - nums[i]
            count += 1
        return num
        
        