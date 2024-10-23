class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            if count[num] == 2:
                return num
        return -1
        