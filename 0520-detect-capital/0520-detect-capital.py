class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        import re
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
            