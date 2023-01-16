class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_l, t_l = len(s), len(t)
        i, j = 0, 0
        while i < t_l and j < s_l:
            if s[j] == t[i]:
                j += 1
            i +=1
        return j == s_l
        