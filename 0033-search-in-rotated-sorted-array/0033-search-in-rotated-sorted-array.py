class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[right] >= nums[middle]:
                    if target < nums[middle] or target > nums[right]:
                        right = middle - 1
                    else:
                        left = middle + 1
        return -1 

        