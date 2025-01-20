class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        results = []
        total = 0
        for cost1, cost2 in costs:
            results.append([cost2-cost1, cost1, cost2])
        results.sort()
        size = len(results)
        for i in range(size):
            if i < size // 2:
                total += results[i][2]
            else:
                total += results[i][1]
        return total