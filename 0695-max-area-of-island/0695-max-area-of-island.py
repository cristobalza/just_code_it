class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = float('-inf')
        visited = set()
        m, n = len(grid), len(grid[0]) # total rows, total cols
        self.check = lambda r,c: 0 <= r < m and 0<= c < n and grid[r][c] == 1 and (r, c) not in visited 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    self.area = 0
                    self.dfs(r, c, grid, visited)
                    res = max(self.area, res)
        return res if res > 0  else 0
    
    def dfs(self, r, c, grid, visited):
        if self.check(r, c):
            self.area += 1
            visited.add((r,c))
            for ar, ac in [(r+1,c), (r-1,c), (r,c+1),(r,c-1)]:
                self.dfs(ar, ac, grid, visited)