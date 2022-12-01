class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] >= 0 else nums[i]
        return max(dp)
        