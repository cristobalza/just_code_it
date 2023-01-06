class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        
        for num in nums:
            dp[num] = 1
        
        for i, val in enumerate(dp):
            if val == 0: return i