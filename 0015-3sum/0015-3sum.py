class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx -  1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = val + nums[left] + nums[right]
                if total == 0:
                    results.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return results