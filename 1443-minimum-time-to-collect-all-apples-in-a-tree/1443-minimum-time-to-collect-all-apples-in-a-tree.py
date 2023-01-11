class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {node: [] for node in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(node, prev):
            for neigh in graph[node]:
                if neigh != prev and dfs(neigh, node):
                    hasApple[node] = True 
            return hasApple[node]
        dfs(0, None)
        return (sum(hasApple)) * 2 - 2*(hasApple[0])
        
        