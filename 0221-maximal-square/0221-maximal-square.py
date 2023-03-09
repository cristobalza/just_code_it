'''
do some sort of bfs
 - bfs up left, bfs up right, bfs down left, bfs down right
 
 [["0","1","1","1","0"],
  ["0","1","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1,"1","1","0"]]


'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
                