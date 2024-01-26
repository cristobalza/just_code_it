class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        memo = [0] * len(nums)
        memo[0] = nums[0]
        for i in range(1, len(nums)):
            if memo[i-1] > 0:
                memo[i] = max(memo[i-1] - 1, nums[i])
        return any(memo[-2:]) > 0
        