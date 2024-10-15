class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        results = []
        part_length = len(part)
        for character in s:
            results.append(character)
            if len(results) >= part_length and ''.join(results[-part_length:]) == part:
                results[-part_length:] = []
        return ''.join(results)



            
        