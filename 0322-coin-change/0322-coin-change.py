class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf')] * (amount + 1)
        memo[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0: # conitnue searching
                    memo[i] = min(memo[i], memo[i - coin] + 1)
                    # coin = 4
                    # i = 7
                    # memo[7] = 1 + memo[7-4]
        return memo[amount] if memo[amount] != float('inf') else -1