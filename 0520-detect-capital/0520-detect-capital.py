class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n == 1:
            return True
        
        if word[0].isupper() and word[1].isupper():
            for i in range(2, n):
                if not word[i].isupper():
                    return False
        elif word[0].isupper() and not word[1].isupper():
             for i in range(2, n):
                if word[i].isupper():
                    return False
        elif not word[0].isupper():
            for i in range(1, n):
                if word[i].isupper():
                    return False
        return True
            