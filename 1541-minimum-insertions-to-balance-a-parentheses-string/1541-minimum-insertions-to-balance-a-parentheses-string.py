class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        total = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if i + 1 < len(s) and s[i+1] == ')':
                    i += 1
                else:
                    total += 1
                if stack:
                    stack.pop()
                else:
                    total += 1
            i += 1
        return len(stack) * 2 + total