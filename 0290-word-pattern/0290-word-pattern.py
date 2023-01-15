class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2letter = {}
        s = s.split()
        if len(s) != len(pattern): return False
        if len(set(s)) != len(set(pattern)): return False
        for i in range(len(s)):
            if s[i] not in word2letter:
                word2letter[s[i]] = pattern[i]
                continue
            elif word2letter[s[i]] != pattern[i]:
                return False
        return True