class Solution:
    def longestPalindrome(self, s: str) -> str:
        # have a function where I see if its a palindrome 
        def is_palindrome(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1   
            return s[left + 1: right]

        longestString = ""
        for i in range(len(s)):
            result1 = is_palindrome(i,i)
            if len(result1) > len(longestString):
                longestString = result1
            result2 = is_palindrome(i, i + 1)
            if len(result2) > len(longestString):
                longestString = result2
        return longestString