class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        column_number = 0

        if n <= 1:
            return ord(columnTitle) - 64
        
        for character in columnTitle:
            column_number += (ord(character) - 64) * (26 ** (n - 1))
            n -= 1
        return column_number