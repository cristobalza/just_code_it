class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        x return sqrt(x)
        
        x = 4 -> 2
        
        4 ** 1/2 = 2
        4 = 2 ** 2
        4 = 2 * 2
        
        
        x = 64
     64 ** 1/ 2 = 8
     
     
        0 ---32---- 64
        l   m     r
        '''
        
        if x < 2: return x
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid+1):
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid
                
        
        
        