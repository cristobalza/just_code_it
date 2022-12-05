class Solution:
    def numSquares(self, n: int) -> int:
        '''
        n = 12
        
        sqrt(12) = between 3 and 4
        
        int(sqrt(12)) = 3
        
        for i in range(int(sqrt(12) + 1)):
             sqrt_arr.append(i ** 2)
             
        dp = [float('inf')] * n + 1
        dp[0] = 0
        
        for i in range(1, n + 1):
        
        '''
        square_nums = [i**2 for i in range(int(sqrt(n)) + 1)]
        dp = [0] + [float('inf')] * n
        for i in range(1, n + 1):
            for p_s in square_nums:
                if i < p_s:
                    break
                dp[i] = min(dp[i], dp[i-p_s] + 1)
        return dp[-1]