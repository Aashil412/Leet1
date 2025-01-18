class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        array = [0] * 1001
        for trip in trips:
            currPass, start, end = trip
            array[start] += currPass
            array[end] -= currPass

        currentPass = 0
        for i in range(1001):
            currentPass += array[i]
            if currentPass > capacity:
                return False
        return True
