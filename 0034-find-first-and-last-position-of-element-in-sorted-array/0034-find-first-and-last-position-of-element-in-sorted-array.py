class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.n, self.nums, self.target = len(nums), nums, target
        if self.n == 1: return [0,0] if self.nums[0] == self.target else [-1,-1]
        return [self.binary_search(True), self.binary_search(False)]
    def binary_search(self, isLeft):
        l, r, idx = 0, self.n - 1, -1
        while l <= r:
            m = (l + r) // 2
            if self.nums[m] == self.target:
                idx = m
                if isLeft:
                    r = m - 1
                else:
                    l = m + 1
            elif self.nums[m] < self.target:
                l = m + 1
            else:
                r = m - 1
        return idx