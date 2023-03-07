class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs, res, n, i, j = set(), 0, len(s), 0, 0
        while j < n:
            while s[j] in hs:
                hs.remove(s[i])
                i += 1
            hs.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res
        
        