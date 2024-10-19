class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for index in range(len(number)):
            if number[index] == digit:
                max_num = max(max_num, int(number[:index] + number[index+1:]))
        return str(max_num)
