class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        dp = [1]
        while len(res) < numRows:
            prev = dp # prev row
            dp = [1] * (len(prev)+1) # new
            for i in range(len(prev) + 1):
                if i == 0 or i == len(prev):
                    continue
                else:
                    dp[i] = prev[i - 1] + prev[i]
            res.append(prev)
        return res
            
            
                