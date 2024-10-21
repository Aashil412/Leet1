class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for neighbor in graph[source]:
                    if dfs(neighbor, target):
                        return True

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u,v):
                return [u,v]
            graph[u].add(v)
            graph[v].add(u)
