class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenNum_at_odd_index = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 != 0: # if there is a odd number at even index
                while nums[evenNum_at_odd_index] % 2 != 0: # check if even num in odd index
                    evenNum_at_odd_index += 2
                nums[i], nums[evenNum_at_odd_index] = nums[evenNum_at_odd_index], nums[i]
        return nums
