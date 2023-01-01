class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2letter = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False
        
        for i, word in enumerate(words):
            if word not in word2letter:
                word2letter[word] = pattern[i]
                continue
            elif word2letter[word] != pattern[i]:
                return False
        return True
            