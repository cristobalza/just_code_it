class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num2freq = collections.Counter(nums)
        sorted_freq_arr = sorted(num2freq.values(), reverse=False)
        sorted_num_arr = sorted(num2freq.keys(), reverse=True)
        
        res = []
        
        for f in sorted_freq_arr:
            for n in sorted_num_arr:
                if num2freq[n] == f:
                    res.extend([n] * f)
                    del num2freq[n]
        return res
        