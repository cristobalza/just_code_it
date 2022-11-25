class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(summ, i, subset):
            if summ == target:
                res.append(subset[::])
                return
            elif summ > target:
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                    
                summ += candidates[j]
                subset.append(candidates[j])
                
                backtrack(summ, j + 1, subset)
                
                summ -= candidates[j]
                subset.pop()
                
                prev = candidates[j]
            return 
        
        # run
        candidates.sort()
        backtrack(0, 0, [])
        return res
        
            
        