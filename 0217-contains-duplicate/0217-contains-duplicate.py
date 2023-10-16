class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for val in nums:
            if val in hs:
                return True
            hs.add(val)
        return False