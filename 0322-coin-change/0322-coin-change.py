class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        given coins array, amount integer
        
        R: fewest number of coins you need to make up the amount
        
         [1, 2, 5] , 11
         
         [1, 2, 5]
          i
          
          1 1 1 1 1 1 1 1 1 1 1 ~ 11 
          1 2 1 2 1 2 1 1 ~ 8 
          5 2 2 1 1 
          .
          .
          .
          5 5 1
          
          
        """
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if 0 <= i - c < amount+1:
                    dp[i] = min(1 + dp[i - c], dp[i])
        return dp[-1] if dp[-1] != float("inf") else -1