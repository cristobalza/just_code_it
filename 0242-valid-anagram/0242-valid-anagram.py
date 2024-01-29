class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = collections.Counter(s), collections.Counter(t)
        return True if s_counter == t_counter else False
        