class Solution:
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        for i in range(len(nums)):
            total *= nums[i]
        def signFunc(product):
            if total > 0:
                return 1
            elif total < 0:
                return -1
            else:
                return 0
        return signFunc(total)
