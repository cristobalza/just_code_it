'''
s = "aba"
      i
     aa -> check - return true
         *. *
     "abcosdodfg"
            r
         l
         
     def helper(l,r):
        if l < r:
        if s[l ] == s[r]:
            return helper(l -1,r-1)
        else:
            return False

'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        check = lambda s :s[::-1] == s
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return check(s[l:r]) or check(s[l+1:r+1])
        return True
                

            
        