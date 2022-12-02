class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        subset = [1]
        while len(res) < numRows:
            prev = subset
            res.append(prev)
            subset = []
            for i in range(len(prev) + 1):
                if i == 0 or i == len(prev):
                    subset.append(1)
                else:
                    subset.append(prev[i-1] + prev[i])
        return res
            
            
                