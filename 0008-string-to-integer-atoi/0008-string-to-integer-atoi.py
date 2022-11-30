class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
        idx = 0
        if s[idx] == '-' or s[idx]=="+":
            idx += 1
        res = 0
        while idx < len(s) and s[idx].isdigit():
            # print(ord(s[idx])  - ord('0'))
            # print(res*10 + (ord(s[idx])  - ord('0')))
            res = res*10 + (ord(s[idx])  - ord('0'))
            idx += 1
        
        res *= sign
        return res if -2**31 <= res <= 2**31 - 1 else (-2**31 if res < -2**31 else 2**31 - 1)