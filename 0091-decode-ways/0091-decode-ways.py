class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[-1] = 1
        check=lambda num: 1<= num <= 26
        for i in range((n+1)-2, -1, -1):
            if s[i] == '0':
                continue
            if i + 1 < (n+1):
                dp[i] += dp[i+1]
            if i + 2 < (n+1) and check(int(s[i:i+2])):
                dp[i] += dp[i+2]
        return dp[0]