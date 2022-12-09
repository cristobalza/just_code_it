class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n <= 2:
            return max(max(nums), sum(nums))
        dp= [0]*n
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = dp[i-1] + nums[i] if dp[i-1] >= 0 else nums[i]
        
        return max(dp)
        