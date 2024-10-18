class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for x, y in coordinates:
            #colinear
            if (y2-y1) * (x1-x) != (y1-y) * (x2-x1):
                return False
        return True
