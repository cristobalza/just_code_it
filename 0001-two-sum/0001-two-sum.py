class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        hm = {7:0, }
        
        9 - 2
        9-7
        
        nums = [2,7,11,15], target = 9
                  i 
        '''
        hm = {}
        for i, num in enumerate(nums):
            if target - num in hm:
                return [hm[target - num], i]
            hm[num] = i