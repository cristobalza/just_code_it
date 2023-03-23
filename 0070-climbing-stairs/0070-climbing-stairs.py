'''
Given n : int

each move is 1 or 2

R: number of different distinct wat to climb the top

n = 2
   01
   11
   
         n=2
         
    1                                 2
    
2       3notpossible                


n = 5.  

                           
                          n
                          
                      1         2
              2           3   3.   4
          3     5        4 5  4 5  5 
         4  5           5    5
       5
       
dynamic programming
- create a n array of 0
- first and second vals are 1 and 2
- iterate through n from 2
  - add last and previous to last vals and store at i
- return last 
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]