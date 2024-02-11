class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4]
        
        [1,2,6,8]
        
        
        
        '''
        memo = [1]  * len(nums)
        postfix = 1
        for i in range(len(nums)):
            memo[i] *= postfix
            postfix *= nums[i]
        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            memo[i] *= prefix
            prefix *= nums[i]
        return memo