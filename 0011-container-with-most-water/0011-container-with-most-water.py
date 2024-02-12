class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = float("-inf")
        area = lambda x1,x2,y1,y2 : min(y2, y1) * (x2 - x1)
        while i < j:
            curr_area = area(i, j, height[i], height[j])
            res = max(res, curr_area)
            if height[j] > height[i]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i+=1
                j-=1
        return res
            
        