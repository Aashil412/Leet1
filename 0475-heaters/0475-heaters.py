class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        # 1, 2, 3
        # -inf, 2, inf
        i = 1
        radius = 0
        for house in houses:
            while heaters[i] < house:
                i += 1
            min_distance = min(house - heaters[i-1], heaters[i] - house)
            radius = max(radius, min_distance)
        return radius
        
    