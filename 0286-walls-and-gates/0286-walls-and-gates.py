class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        q = collections.deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        check = lambda r,c: 0<=r<m and 0<=c<n and rooms[r][c] != 0 and rooms[r][c] != -1
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    q.append((r,c))
        while q:
            r, c = q.popleft()
            dist = 1 + rooms[r][c]
            for x, y in directions:
                adj_r, adj_c = r+x, c+y
                if check(adj_r, adj_c) and dist < rooms[adj_r][adj_c]:
                    q.append((adj_r, adj_c))
                    rooms[adj_r][adj_c] = dist
        
                