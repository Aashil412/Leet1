class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            r = n % 3
            if r == 2:
                return False
            n //= 3
        return True
    