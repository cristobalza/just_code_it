class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ''
        check=lambda b,f: b + 1 < n and f - 1 >= 0 and dp[b + 1][f - 1] == True
        # diagonal 
        for i in range(n):
            dp[i][i] = True
        for back in range(n-1, -1, -1):
            for fwd in range(n):
                if s[back] == s[fwd] and (check(back, fwd) or fwd - back + 1 <= 2):
                    dp[back][fwd] = True
                    if fwd - back + 1 > len(res):
                        res = s[back:fwd+1]
        return res
                