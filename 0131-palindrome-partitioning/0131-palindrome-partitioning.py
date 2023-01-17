class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        check=lambda s: s == s[::-1] if n > 0 else False
        if n == 1: return [[s]]
        res = []
        def backtrack(i, subset):
            # solution
            if i == n:
                res.append(subset[::])
            for j in range(i, n):
                curr = s[i:j+1]
                if check(curr):
                    subset.append(curr)
                    backtrack(j+1, subset)
                    subset.pop()
        backtrack(0, [])
        return res
            
            
            
            