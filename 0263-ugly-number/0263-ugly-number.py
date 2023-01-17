class Solution:
    def isUgly(self, n: int) -> bool: 
        if n <= 0: return False
        
        def helper(dividend, divisior):
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend
        
        for divisor in [2, 3, 5]:
            n = helper(n, divisor)
        return n == 1
        