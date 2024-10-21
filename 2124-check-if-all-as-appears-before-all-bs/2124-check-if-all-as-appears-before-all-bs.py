class Solution:
    def checkString(self, s: str) -> bool:
        if_B = False
        for char in s:
            if char == 'b':
                if_B = True
            if if_B and char == 'a':
                return False
        return True