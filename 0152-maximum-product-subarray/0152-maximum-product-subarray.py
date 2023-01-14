class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1], nums[0] * nums[1])
        dp = [0]*n
        dp[0] = maxima = minima = nums[0]
        for i in range(1, n):
            maxima, minima = max(nums[i], maxima*nums[i], minima*nums[i]), min(nums[i], maxima*nums[i], minima*nums[i])
            dp[i] = max(dp[i-1], maxima, minima)
        print(dp)
        return dp[-1]
            