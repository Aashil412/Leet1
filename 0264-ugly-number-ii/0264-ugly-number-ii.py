class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        # have three indexs and only increment if it is the minimum 
        # 1 2
        multiply_by_2, multiply_by_3, multiply_by_5 = 0, 0, 0
        for i in range(1, n):

            next_num = min(nums[multiply_by_2] * 2, # 1 
                           nums[multiply_by_3] * 3, # 0
                           nums[multiply_by_5] * 5) # 0
            nums.append(next_num)
            if next_num == nums[multiply_by_2] * 2:
                multiply_by_2 += 1
            if next_num == nums[multiply_by_3] * 3:
                multiply_by_3 += 1
            if next_num == nums[multiply_by_5] * 5:
                multiply_by_5 += 1
        return nums[n - 1]