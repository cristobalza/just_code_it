class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount +1
        dp = [float('inf')]*n
        dp[0] = 0
        for coin in coins:
            for i in range(coin, n):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1