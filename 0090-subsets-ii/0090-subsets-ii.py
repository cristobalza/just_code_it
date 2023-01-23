class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        nums.sort()
        res = []
        n = len(nums)
        def backtrack(i, subset):
            if i >= n:
                if tuple(subset) not in visited:
                    visited.add(tuple(subset[::]))
                    res.append(subset[::])
                return
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            
            subset.pop()
            backtrack(i + 1, subset)
            
            return
        backtrack(0, [])
        return res
            
        
        