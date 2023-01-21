class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [0] * n
        dp[0] = maxima = minima = nums[0]
        for i in range(1, n):
            maxima, minima = max(nums[i], maxima * nums[i], minima * nums[i]), min(nums[i], maxima * nums[i], minima * nums[i])
            dp[i] = max(minima, maxima, dp[i-1])
        return dp[-1]
        