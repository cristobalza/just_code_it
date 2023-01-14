class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num2count = collections.Counter(nums)
        tuple_arr = [(num,  count) for num, count in num2count.items()]
        tuple_arr.sort(key=lambda x : x[0], reverse=True)
        tuple_arr.sort(key=lambda x : x[1])
        res = [n for n, c in tuple_arr for _ in range(c)]
        return res