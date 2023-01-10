class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            # print(f'pre :{dp} i: {i}, i+nums[i]+1: {i+nums[i]+1}')
            dp[i] = any(dp[i:i+nums[i]+1])
            # print(f'post:{dp}')

        return dp[0]
        