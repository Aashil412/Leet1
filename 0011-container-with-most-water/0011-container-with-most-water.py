class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        most_water = 0
        while left < right:
            most_water = max(most_water, min(height[left], height[right]) * (right - left))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return most_water