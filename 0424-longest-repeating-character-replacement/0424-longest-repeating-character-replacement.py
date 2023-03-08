class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        res, left, right = 0, 0, 0
        
        while right < len(s):
            hm[s[right]] += 1
            distance = (right - left) + 1
            max_count = max(hm.values())
            
            while ((right - left) + 1) - max_count > k:
                hm[s[left]] -= 1
                left += 1
            res = max(res, ((right - left) + 1))
            right += 1
        return res