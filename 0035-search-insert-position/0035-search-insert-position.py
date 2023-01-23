class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > max(nums):
            return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m
        return l