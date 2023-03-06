class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, hs = len(s), set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if s[j:i] in hs and dp[j]:
                    dp[i] = True
                    break
        print(dp)
        return dp[-1]