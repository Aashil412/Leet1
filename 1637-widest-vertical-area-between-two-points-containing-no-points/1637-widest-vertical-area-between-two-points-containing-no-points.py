class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_axis = []
        for x, y in points:
            x_axis.append(x)
        
        x_length = len(x_axis)
        max_width = 0
        x_axis.sort()
        for i in range(1, x_length):
            difference = x_axis[i] - x_axis[i-1]
            if difference > max_width:
                max_width = difference
        return max_width
        