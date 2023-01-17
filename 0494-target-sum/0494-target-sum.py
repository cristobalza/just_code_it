class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        if n==1: 1 if nums[0] == target else 0
        dp = {}
        def backtrack(i, currsum):
            nonlocal n
            if i == n: return 1 if currsum == target else 0
            if (i, currsum) in dp: return dp[(i, currsum)]
            dp[(i, currsum)] = backtrack(i+1, currsum + nums[i]) + backtrack(i+1, currsum - nums[i])
            return dp[(i, currsum)]
        
        return backtrack(0, 0)
        