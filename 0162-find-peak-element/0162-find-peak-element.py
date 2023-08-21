class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # maxheap
        maxheap = []
        for i, val in enumerate(nums):
            heapq.heappush(maxheap, (-val,i))
        return heapq.heappop(maxheap)[1]