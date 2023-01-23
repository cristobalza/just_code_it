class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_one = ''
        for val in digits:
            plus_one += str(val)
        plus_one = str(int(plus_one) + 1)
        res = [int(plus_one[i]) for i in range(len(plus_one))]
        return res

        