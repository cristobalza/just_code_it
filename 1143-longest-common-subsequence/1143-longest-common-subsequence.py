class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        text1 = '?' + text1
        text2 = '?' + text2
        
        for r in range(1, len(text1)):
            for c in range(1, len(text2)):
                if text1[r] == text2[c]: 
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r-1][c])
                    
        return dp[-1][-1]
                    