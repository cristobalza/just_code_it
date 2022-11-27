class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            r = len(nums) - 1
            mid =  l + 1
            while mid < r:
                summ = nums[l] + nums[mid] + nums[r]
                if summ > 0:
                    r-=1
                elif summ < 0:
                    mid += 1
                else:
                    res.append([nums[l], nums[mid],  nums[r]])
                    mid += 1
                    while mid < r and nums[mid] == nums[mid-1]:
                        mid += 1
        return res