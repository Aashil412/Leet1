class Solution:
    def partitionString(self, s: str) -> int:
        char_set = set()
        left = 0
        count = 0
        for right in range(len(s)):
            if s[right] in char_set:
                count += 1
                while left < right:
                    char_set.remove(s[left])
                    left += 1
            char_set.add(s[right])

        return count + 1
        