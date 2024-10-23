class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # mark the index of the num we visted negative
        results = []
        for num in nums:
            index = abs(num) - 1 
            if nums[index] < 0:
                results.append(index + 1)
            else:
                nums[index] = -nums[index]
        return results
        #index = 5
        #[4,-3,-2,-7,8,2,-3,-1] 
        #[4,3,2,7,8,2,3,1]