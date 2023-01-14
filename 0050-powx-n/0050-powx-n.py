class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursion(x, exp):
            if x == 1 or exp == 0: return 1
            if x == 0: return 0
            if exp == 1: return x
            return recursion(x * x,   exp //2) if exp % 2 == 0 else recursion(x, exp - 1 ) * x
        return recursion(x, n) if n>0 else 1/ recursion(x, abs(n))