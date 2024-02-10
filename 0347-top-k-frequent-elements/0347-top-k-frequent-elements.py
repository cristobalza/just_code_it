class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums = [1,1,1,2,2,3], k = 2
        
        '''
        res = []
        maxheap = []
        counter_mapping = collections.Counter(nums)
        # for num, count in counter_mapping.items():
        #     heapq.heappush(maxheap, (-count, num))
        maxheap = [(-count, num) for num, count in counter_mapping.items()]
        heapq.heapify(maxheap)
        while k > 0 and maxheap:
            _,  num = heapq.heappop(maxheap)
            res.append(num)
            k -= 1
        return res
            
        