class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] * nums[1])
        dp = [0]*len(nums)
        dp[0] = maxx = minn = nums[0]
        for i in range(1, len(nums)):
            maxx, minn = max(nums[i], nums[i] * maxx, nums[i] * minn), min(nums[i], nums[i] * maxx, nums[i] * minn)
            dp[i] = max(maxx, minn, dp[i-1])
        return dp[-1]
        