class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for idx, val in enumerate(nums):
            if val > 0:
                break
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + val
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return results 
        