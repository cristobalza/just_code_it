class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]
        
        area = lambda x, y: x*y
        
        res = 0
        
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, area(height,( (i - index))))
                start = index
            stack.append((start, h))

        for i, h in stack:
            res = max(res, area(h,( (len(heights)  - i))))
        
                
        return res
                
            