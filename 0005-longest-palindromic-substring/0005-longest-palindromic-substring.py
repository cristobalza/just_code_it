class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = s[-1]
        check = lambda r, c : (r + 1 < n and c-1 >= 0 and dp[r + 1][c - 1] == True)
        for i in range(n):
            dp[i][i] = True
        for r in range(n - 1, -1, -1):
            for c in range(n):
                if s[r] == s[c]  and (check(r, c)  or c - r + 1 <=2):
                    dp[r][c] = True
                    # check update
                    if c-r + 1 > len(res):
                        res = s[r:c +1]
        return res
        
        
        