class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4]
        
        prefix = [1,2,6,24]
        
        postfix = [24, 24, 12, 4]
        
        [1*24, 1*12, 2*4=8, 6*1] = [24, 12, 8, 6]
        
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