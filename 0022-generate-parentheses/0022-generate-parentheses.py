class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.limit = n * 2
        self.res = []
        self.backtrack(n, n, [])
        return self.res
    
    def backtrack(self, start, end, subset):
        if start == end == 0:
            self.res.append("".join(subset))
            return
         
        if start > 0:
            subset.append('(')
            self.backtrack(start - 1, end, subset)
            subset.pop()
        if end > 0 and start < end:
            subset.append(')')
            self.backtrack(start, end - 1, subset)
            subset.pop()
            
            
            

        
            