class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {node:[] for node in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            if node == destination:
                return True
            visited.add(node)
            for neigh in graph[node]:
                if neigh != prev and dfs(neigh, node):
                    return True
            return False
            
        return dfs(source, None)
        
            