class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_map = {}
        max_heap = []
        results = ""

        for character in s:
            frequency_map[character] = frequency_map.get(character, 0) + 1
                   
        for key, value in frequency_map.items():
            heapq.heappush(max_heap, (-1 * value, key))

        while max_heap:
            value, key = heapq.heappop(max_heap)
            value = -1 * value
            while value > 0:
                results += key
                value -= 1
        return results 