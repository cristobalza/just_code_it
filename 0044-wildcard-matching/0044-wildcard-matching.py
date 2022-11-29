class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        needle, haystack = s, p
        
        dp = [[False for _ in range(len(haystack) + 1) ] for _ in range(len(needle) + 1)]
        dp[0][0] = True
        for j in range(1, len(haystack) + 1):
            if haystack[j-1] != '*':
                break
            dp[0][j] = True
        
        for r in range(1, len(needle) + 1):
            for c in range(1, len(haystack) + 1):
                if haystack[c-1] == '?' or needle[r-1] == haystack[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                elif p[c-1] == '*':
                    dp[r][c] = dp[r-1][c] or dp[r][c-1]
                else:
                    continue
        
        return dp[-1][-1]
        