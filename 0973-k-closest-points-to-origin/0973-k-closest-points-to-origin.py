class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []
        max_heap = []
        for x, y in points:
            distance = sqrt(x**2 + y **2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, [x,y]))
            else:
                if distance < -max_heap[0][0]:
                    print(max_heap[0][0])
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-distance, [x,y]))
        return [p for _, p in max_heap]