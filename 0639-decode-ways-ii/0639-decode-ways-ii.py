class Solution:
    def numDecodings(self, s: str) -> int:
        M = 10**9 + 7 
        
        @lru_cache(None)
        def dp(i):
            if i < 0: return 1
            if s[i] == "*":
                corr = {"1": 9, "2": 6, "*":15}
                ans = 9*dp(i-1)
                if i > 0: 
                    ans += corr.get(s[i-1], 0)*dp(i-2)
                return ans % M
            
            ans = dp(i-1) if s[i] != "0" else 0
            if i > 0 and "10" <= s[i-1:i+1] <= "26":
                ans += dp(i-2)
            elif i > 0 and s[i-1] == "*":
                ans += (2 if s[i] <= "6" else 1)*dp(i-2)
            
            return ans % M
        
        return dp(len(s)-1) % M

        