class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        size = len(nums)
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
            if counter[num] > size / 2:
                return num
        return -1  
        