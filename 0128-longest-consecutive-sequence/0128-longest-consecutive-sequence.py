class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        results = set(nums)
        maxLength = 0
        for num in results:
            if num - 1 not in results:
                current_max = 1
                while num + 1 in results:
                    current_max += 1
                    num += 1
                maxLength = max(maxLength, current_max)
        return maxLength

        