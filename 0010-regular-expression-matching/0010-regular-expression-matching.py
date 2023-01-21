class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        is_match=lambda row, col: row < len(s) and (s[row] == p[col] or p[col] == "." )
        for row in range(len(s), -1, -1):
            for col in range(len(p) - 1, -1, -1):
                if (col + 1) < len(p) and p[col+1] == '*':
                    dp[row][col] = dp[row][col + 2]
                    if is_match(row, col):
                        dp[row][col] = dp[row + 1][col] or dp[row][col]
                elif is_match(row, col):
                    dp[row][col] = dp[row + 1][col + 1]
                    
        print(dp)
        return dp[0][0]