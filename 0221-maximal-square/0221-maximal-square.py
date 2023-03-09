'''

[["1","0","1","0","0"], 
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]

  0. 1. 2. 3. 4. 5
0[[0, 0, 0, 0, 0, 0],
1 [0, 1, 0, 1, 0, 0],
2 [0, 1, 0, 1, 1, 1], 
3 [0, 1, 1, 1, 2, 2], 
4 [0, 1, 0, 0, 1, 0]]


'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        max_side = 0
        
        for r in range(1,m+1):
            for c in range(1,n+1):
                if matrix[r-1][c-1] == '1':
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1 
                    max_side = max(max_side, dp[r][c])
        print(dp)
        return max_side * max_side
                