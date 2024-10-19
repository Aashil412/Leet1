class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        radius = 0
        for house in houses:
            position_of_heater = self.binary_search(heaters, house)
            
            if position_of_heater == 0:
                left_heater = float('inf')
            else:
                left_heater = house - heaters[position_of_heater - 1]

            if position_of_heater == len(heaters):
                right_heater = float('inf')
            else:
                right_heater = heaters[position_of_heater] - house 
            
            min_distance = min(left_heater, right_heater)
            radius = max(radius, min_distance)
        return radius
        
        
    def binary_search(self, heaters, house): # calculate the first heater to the right or equal to the house
        left, right = 0, len(heaters) - 1
        while left<=right:
            middle = (left + right) // 2
            if heaters[middle] < house:
                left = middle + 1
            else:
                right = middle - 1
        return left 
    
        
    