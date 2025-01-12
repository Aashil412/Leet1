class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.original_nums = nums[:]

    def reset(self) -> List[int]:
        return self.original_nums

    def shuffle(self) -> List[int]:
        size = len(self.array)
        for i in range(size):
            j = random.randrange(i, size)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()