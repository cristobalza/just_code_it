class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        max_ =min_ = dp[0] = nums[0]
        for i in range(1, n):
            max_, min_ = max(max_*nums[i], min_*nums[i], nums[i]), min(max_*nums[i], min_*nums[i], nums[i])
            dp[i] = max(max_, min_, dp[i-1])
        return max(dp)