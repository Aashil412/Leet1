class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
        min_heap = []
        apples_eaten = 0
        i = 0
        while i < len(apples) or min_heap:
            
            if i < len(apples):
                apples_left = apples[i]
                if apples_left > 0:
                    days_until_rotten = i + days[i]
                    heapq.heappush(min_heap, (days_until_rotten, apples_left))

            while min_heap and (min_heap[0][0] <= i or min_heap[0][1] == 0):
                heapq.heappop(min_heap)
            
            if min_heap:
                rotten_day, remaining_apples = heapq.heappop(min_heap)
                remaining_apples -= 1
                apples_eaten += 1
                if remaining_apples > 0:
                    heapq.heappush(min_heap, (rotten_day, remaining_apples))
            i += 1
        return apples_eaten