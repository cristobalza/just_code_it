class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2**31 - 1
        m, n = len(rooms), len(rooms[0])
        check=lambda r,c: 0<= r < m and 0<= c < n and rooms[r][c] != -1 and rooms[r][c] != 0
        # collect gates
        q = collections.deque()
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r,c))
        # bfs
        while q:
            r,c = q.popleft()
            dist = rooms[r][c] + 1
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                if not check(r+x, c+y):
                    continue
                if dist < rooms[r+x][c+y]:
                    rooms[r+x][c+y] = dist
                    q.append((r+x, c+y))
        
                    
                
                    
