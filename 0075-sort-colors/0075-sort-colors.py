class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        """
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b-= 1
            elif nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                r += 1
                w += 1 
            else:
                w += 1               
