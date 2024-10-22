class Solution:
    def partitionString(self, s: str) -> int:
        left, right = 0, 1
        count = 0
        while right < len(s):
            if s[right] == s[left]:
                count += 1
                left = right
                right += 1
            else:
                right += 1
        return count + 1
        