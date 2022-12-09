class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n =len(nums)
        if n == 1:
            return True 
        prev =nums[0]
        
        for i in range(1, n):
            curr=nums[i]
            if prev == 0:
                return False
            curr, prev =prev, max(prev - 1, curr) 
            
        return prev >= 1 or curr >= 0