class Solution:
    def isValid(self, s: str) -> bool:
        parenthisis = {')': '(', ']': '[', '}':'{'}
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif not stack or parenthisis[char] != stack[-1]:
                return False
            else:
                stack.pop()
        return len(stack) == 0 
        