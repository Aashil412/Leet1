class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        def compareStr(n1, n2):
            return -1 if n1 + n2 > n2 + n1 else 1
        nums = sorted(nums, key = cmp_to_key(compareStr))

        return "0" if nums[0] == "0" else "".join(nums)