class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sen = ""
        for char in s:
            sen += str(ord(char) - ord('a') + 1)
        
        while k > 0:
            temp = 0
            for x in sen:
                temp += int(x)
            sen = str(temp)
            k -= 1
        return int(sen)

            
        