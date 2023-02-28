class Solution:
    def myPow(self, x: float, n: int) -> float:        
        memo = {}
        def helper(x, n):
            if n == 1: return x
            if n == 0: return 1
            if x in memo: return memo[x]
            memo[x] = helper(x*x, n // 2) if n % 2 == 0 else x * helper(x, n-1)
            return memo[x]
        return helper(x, n) if n > 0 else 1 / helper(x, abs(n))
    