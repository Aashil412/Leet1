class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            map[num] = map.get(num, 0) + 1
        for key, val in map.items():
            freq[val].append(key)
        results = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results
        
        

        