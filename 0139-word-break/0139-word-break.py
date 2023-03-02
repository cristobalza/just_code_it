class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hs = set(wordDict)  
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                word = s[j:i]
                if word in hs and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]