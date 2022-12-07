class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        dp = [[False] * n for _ in range(n)]
        
        # diagonal of T
        for i in range(n):
            dp[i][i] = True
        
        res = s[-1]
        # iterate backwards
        # iterate forward with respect to the backward index (O(n^2))
        for back in range(n - 1, -1, -1):
            for fwd in range(back, n):
                # print(f"fwd: {s[fwd]}")
                # print(f"back: {s[back]}")
                if s[fwd] == s[back] :
                    if (back + 1 < n and fwd - 1 >= 0 and dp[back + 1][fwd - 1] is True) or ( fwd - back + 1 <= 2):
                        dp[back][fwd] = True
                        if fwd - back + 1 > len(res):
                            res = s[back:fwd+1]
        return res   
        