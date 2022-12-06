class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        dp = [[False] * n for _ in range(n)]
        
        # diagonal of T
        for i in range(n):
            dp[i][i] = True
            
        res = s[-1]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        word = s[i:j+1]
                        # print(f'i: {i}, j: {j}, -> {dp}')
                        # print(f'word: {word}')
                        if len(res) < len(word):
                            res = word
        return res   
        