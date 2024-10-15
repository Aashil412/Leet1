class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        results = [''] * len(s)
        part_length = len(part)
        j = 0
        for index, character in enumerate(s):
            results[j] = character
            j += 1
            if j >= part_length and ''.join(results[j - part_length:j]) == part:
                j -= part_length
        return ''.join(results[:j])

    #daabcbaabcbc 
    #[d,a,a,b,c,,,,,,,]

            
        