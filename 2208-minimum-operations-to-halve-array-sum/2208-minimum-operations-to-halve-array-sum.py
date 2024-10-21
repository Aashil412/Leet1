class Solution:
    def halveArray(self, nums: List[int]) -> int:
        max_heap = []
        total = 0
        for num in nums:
            total += num
            heapq.heappush(max_heap, -num)
        
        half = total / 2
        operations = 0
        while max_heap and total > half:
            largest = heapq.heappop(max_heap)
            largest *= -1
            largest /= 2
            total -= largest
            operations += 1
            if largest > 0:
                heapq.heappush(max_heap, -largest)
        return operations