class Solution:
    def countDigitOne(self, n: int) -> int:
        ones_count = 0
        base = 1
        #12345
        while base <= n:
            left = n // base // 10
            current = n // base % 10
            right = n % base

            if current > 1:
                ones_count += (left + 1) * base
            elif current == 1:
                ones_count += left * base + right + 1
            else:
                ones_count += left * base
            base *= 10
        return ones_count