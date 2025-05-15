class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        count = 1
        for num in nums:
            actual_sum += count - num
            count += 1
        return actual_sum 