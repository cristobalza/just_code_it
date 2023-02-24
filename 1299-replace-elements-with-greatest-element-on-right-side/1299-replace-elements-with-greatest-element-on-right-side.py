class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # max heap
        # from collections import heapq
        n = len(arr)
        res = []
        maxheap = []
        for i, val in enumerate(arr):
            heapq.heappush(maxheap, (-val, i))
            
        for i in range(n-1):
            while maxheap and  i >= maxheap[0][1]:
                heapq.heappop(maxheap)

            res.append(-1 * maxheap[0][0])
        res.append(-1)
        return res
                
        