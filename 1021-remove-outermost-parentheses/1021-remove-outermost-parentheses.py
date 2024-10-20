class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        results = ""
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0:
                    results += char
                depth += 1
            elif char == ')':
                depth -= 1
                if depth > 0:
                    results += char
        return results