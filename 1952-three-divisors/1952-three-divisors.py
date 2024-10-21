class Solution:
    def isThree(self, n: int) -> bool:
        count = 1
        for i in range(n, 1, -1):
            if n % i == 0:
                count += 1
        return count == 3
            
            