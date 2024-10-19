class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                left_character = s[i-1] if i > 0 else ''
                right_character = s[i+1] if i < len(s) - 1 else ''

                for char in 'abc':
                    if char != left_character and char != right_character:
                        s[i] = char
                        break
        return ''.join(s)


                
                    