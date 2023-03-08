class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        
        sort()
        l, r
        
        [1,2,2,2,3] k= 3
             l
             r
         res = 1
         nums[l] + nums[r] = 2 then res ++ ; if nums[l] + nums[r] < k: r ++ else l ++
        if l == r: 
            if nums[r] == k:
                res ++
                r ++
        elif nums[r] + nums[l] < 
            r ++
        elid num[r] + nums[l] > k
            l ++
            
        else:
            res ++
            l = r
            r ++
        
        [1,1,1]  k = 2
         l
             r
         
         res = 2
         ----
         
         [1,1,1,1,1,2,2,3,3] k = 3
          i
         hm = {0:1}
         sum = 0
         hm[0] = 1
         for i in range(n)
            sum += nums[i]
            if sum - k in hm:
                res += hm[sum-k]
            hm[sum] += 1
        return res
         
        '''

        res, prefsum, hm = 0,  0, {0:1}
        for num in nums:
            prefsum += num
            if  prefsum-k in hm:
                res += hm[prefsum-k]
            hm[prefsum] = hm.get(prefsum, 0) + 1
        return res
                
        
        
        
                
                
                
                
                
                
        