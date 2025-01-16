class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths, current_path = [], [0]
        last_node = len(graph) - 1

        def dfs(current_node):

            if current_node == last_node:
                paths.append(current_path[:])
                return
            
            for neighbors in graph[current_node]:
                current_path.append(neighbors)
                dfs(neighbors)
                current_path.pop()
        dfs(0)
        return paths
        