class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # have a dictionary to see the last occuring index of a char
        # have a stack to see if the top is greater than current and use dictionary to pop stack
        # have a set to see if we seen it before

        last_occuring_character = {}
        for i in range(len(s)):
            last_occuring_character[s[i]] = i
        
        stack = []
        visted = set()
        for i in range(len(s)):
            if s[i] in visted:
                continue
            
            while stack and stack[-1] > s[i] and last_occuring_character[stack[-1]] > i:
                visted.remove(stack[-1])
                stack.pop()
            if s[i] not in visted:
                stack.append(s[i])
                visted.add(s[i])
        return ''.join(stack)

        