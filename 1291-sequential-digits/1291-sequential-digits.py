class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        '''
        
        123456789
        s---|
        
        low = 1000
        high = 13000
        
        
        '''
        s = '123456789'
        string_low = str(low)
        start = int(string_low[0]) - 1
        length = len(string_low) 
        end = length + start
        if end > len(s):
            end = start + 1 if start != len(s) -1 else start
        res = list()
        while end <= len(s):
            num = int(s[start:end])
            if num > high:
                break
            if low <= num:
                res.append(num)
            start += 1
            end += 1
            if end > len(s):
                start = 0
                length += 1
                end = length + start
        return res