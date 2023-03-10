'''
nums1 = [4,9,5], nums2 = [9,4,7,10,11,9,8,4] 
         i

'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hset1, hset2 = set(nums1), set(nums2)
        if len(nums1) < len(nums2):
            return [val for val in hset1 if val in hset2]
        else:
            return [val for val in hset2 if val in hset1]
            
            