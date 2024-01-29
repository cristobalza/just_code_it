class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for num in nums:
            if num in hs:
                return True
            hs.add(num)
        return False