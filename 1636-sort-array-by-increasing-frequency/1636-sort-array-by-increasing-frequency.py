class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num2freq = collections.Counter(nums)
        bag = []
        for n, f in num2freq.items():
            bag.append((n, f))
        bag.sort(key= lambda x : x[0], reverse = True)
        bag.sort(key= lambda x : x[1])
        
        res = []
        for n, f in bag:
            res.extend([n]*f)
        return res
        