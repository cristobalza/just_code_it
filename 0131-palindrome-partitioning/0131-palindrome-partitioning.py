class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        def backtrack(subset, i):
            if i == len(s):
                if len(subset) > 0:
                    res.append(subset[::])
                return
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if self.check(substring):
                    subset.append(substring)
                    backtrack(subset, j+1)
                    subset.pop()
            return 
        
        res = []
        backtrack([], 0)
        return res
                
    def check(self, s):
        return s == s[::-1] if len(s) > 0 else False