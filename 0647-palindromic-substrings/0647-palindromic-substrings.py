class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Create a 2d array len.s by len.s
        Fill out the diagonal with True 
        
        create a count
        iterate backwards and then forward 
        if s[i] == s[j] and either j - i + 1 <= n or dp[i+1][j-1] is True then count++
        return count 
        
        '''
        
        n = len(s)
        if n == 1:
            return 1
        
        dp = [[False]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        count = 0
        for back in range(n - 1, -1, -1):
            for fwd in range(back, n):
                # print(f"fwd: {s[fwd]}")
                # print(f"back: {s[back]}")
                if s[fwd] == s[back] :
                    if (back + 1 < n and fwd - 1 >= 0 and dp[back + 1][fwd - 1] is True) or ( fwd - back + 1 <= 2):
                        dp[back][fwd] = True
                        count += 1
        # print(dp)
        return count
        