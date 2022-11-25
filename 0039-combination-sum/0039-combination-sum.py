class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(summ, i, subset):
            if summ == target:
                res.append(subset[::])
                return
            elif summ > target or i == len(candidates):
                return
            
            subset.append(candidates[i])
            summ += candidates[i]

            backtrack(summ, i, subset)

            subset.pop()
            summ -= candidates[i]

            backtrack(summ, i+1, subset)
            return
        backtrack(0, 0, [])
        return res
                

            
        