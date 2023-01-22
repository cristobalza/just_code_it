class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node, prev):
            if node in visited: return False
            visited.add(node)
            for neigh in graph[node]:
                if prev != neigh and not dfs(neigh, node): return False
            return True
        return True if dfs(0, -1) and len(visited) == n else False