class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                word = s[j:i]
                if dp[j] and word in word_set:
                    dp[i] = True
                    break
        return dp[-1]