'''
not valid ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
             i
             
    
     
     
    valid ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    
for val in enumerate(s):
    if it is a number the isNumber = True
    
    if it is a . then if isDot or val is e or E then return false
    
    if is a + or - then if i > 0 and isSign is False OR isExponent then return False
    
    if it a e or E then if isExponent then return False


'''
class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit, seenExponent, seenDot = False, False, False
        for i, val in enumerate(s):
            if val.isdigit():
                seenDigit =True
            elif val == '+' or val == '-':
                if i > 0 and s[i-1] != 'e' and s[i-1] != 'E': return False
            elif val == 'e' or val == 'E':
                if seenExponent or not seenDigit: return False
                seenExponent = True
                seenDigit = False 
            elif val == '.':
                if seenDot or seenExponent: return False
                seenDot = True
            else:
                return False
        return seenDigit
        