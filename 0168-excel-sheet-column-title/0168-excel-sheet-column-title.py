class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_letters = ""
        while columnNumber:
            columnNumber -= 1
            column_letters = chr(columnNumber % 26 + 65) + column_letters
            columnNumber //= 26
        return column_letters
            