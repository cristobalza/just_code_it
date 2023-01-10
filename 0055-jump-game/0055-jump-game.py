class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        dp = [0] * n
        dp[0] = nums[0]
        if dp[0] == 0: return False
        for i in range(1, n):
            if dp[i-1] == 0:
                return False
            dp[i] = max(dp[i-1] - 1, nums[i])

        return any(dp[-2:]) > 0
        
        