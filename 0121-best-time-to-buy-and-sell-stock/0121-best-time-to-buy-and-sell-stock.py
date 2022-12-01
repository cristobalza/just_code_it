class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        minn = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i] - minn)
            minn = min(minn, prices[i])
        return dp[-1]
        