class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        fwd_dp = [0] * (n)
        fwd_dp[1] = nums[1]
        fwd_dp[2] = max(nums[1], nums[2])
        for i in range(3, n):
            fwd_dp[i] = max(fwd_dp[i-1], nums[i] + fwd_dp[i-2])
            
            
        back_dp = [0] * (n - 1)
        back_dp[0] = nums[0]
        back_dp[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            back_dp[i] = max(back_dp[i-1], nums[i] + back_dp[i-2])
        
        return max(back_dp[-1], fwd_dp[-1])
        
        
        