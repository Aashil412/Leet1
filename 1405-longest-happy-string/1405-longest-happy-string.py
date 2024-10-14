class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #a = 3, b = 0, c = 0
        # aabaa
        if a == 0 and b == 0 and c == 0:
            return ""
        results = ""
        max_heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))
        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(results) > 1 and results[-1] == char and results[-2] == char:
                if not max_heap:
                    break
                count1, char1 = heapq.heappop(max_heap)
                results += char1 
                count1 += 1
                if count1 != 0:
                    heapq.heappush(max_heap, (count1, char1))
            else:
                results += char
                count += 1
            if count != 0:
                heapq.heappush(max_heap, (count, char))
        return results


    