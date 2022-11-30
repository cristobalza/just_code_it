class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        x = 2 , n = 3 => 8
        
        1------------------1024
        
        1-------------8
                   
        
        '''
        res = self.helper(x,abs(n)) if x != 1 else 1
        return res if n >= 0 else 1/res
        
    def helper(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        return self.helper((x*x), n // 2) if n % 2 == 0 else x * self.helper(x, n - 1)
      
            
        