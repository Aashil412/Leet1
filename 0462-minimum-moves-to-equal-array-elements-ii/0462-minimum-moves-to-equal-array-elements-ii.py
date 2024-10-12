class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        middle = len(nums) // 2
        count = 0
        for num in nums:
            if num == nums[middle]:
                continue
            count += abs(nums[middle] - num)
        return count