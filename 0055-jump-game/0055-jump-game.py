class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_goal = len(nums) - 1

        for i in range(current_goal, -1, -1):
            if nums[i] + i >= current_goal:
                current_goal = i
        
        return current_goal == 0
        