class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, subset):
            # solution
            temp = tuple(subset)
            if temp not in res:
                res.add(temp)
            
            for j in range(i, len(nums)):
                # mark candidate
                subset.append(nums[j])
                
                #explore
                backtrack(j + 1, subset)
                
                #remove candidate
                subset.pop()
                
                # explore 2
                backtrack(j + 1, subset)
                
                return
        
        res = set()
        backtrack(0, [])
        return list(res)