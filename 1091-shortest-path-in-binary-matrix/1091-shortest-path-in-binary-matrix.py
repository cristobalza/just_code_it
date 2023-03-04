class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        m, n, res, visited, q = len(grid), len(grid[0]), float('inf'), set(), collections.deque([(0,0,1)])
        visited.add((0,0))
        directions = lambda r, c: [(r+1,c), (r-1,c), (r,c+1), (r,c-1), (r+1, c+1), (r-1, c-1), (r+1, c-1), (r-1, c+1)]
        check = lambda ar, ac: (ar, ac) not in visited and 0 <= ar < m and 0 <= ac < n and grid[ar][ac] == 0
        
        while q:
            r, c, cum_path = q.popleft()
            if r == m - 1 and c == n - 1:
                res = min(res, cum_path)
            for ar, ac in directions(r, c):
                if check(ar, ac):
                    q.append((ar, ac, cum_path + 1))
                    visited.add((ar, ac))
        return res if res != float('inf') else -1
        