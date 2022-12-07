class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1
        
        for i in range(n - 1,  -1, -1):
            if s[i] == '0':
                continue
            if i + 2 <= n and int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
            if i + 1 <= n: # given that it will be less than 26 since only one digit
                dp[i] += dp[i+1]
                
        return dp[0]