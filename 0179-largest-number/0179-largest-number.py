class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(n1, n2):
            return 1 if n1 + n2 <= n2 + n1 else -1
        arr = [str(nums[i]) for i in range(len(nums))]
        arr = sorted(arr, key=cmp_to_key(comparator))
        return str(int("".join(arr)))
