class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousandMillionBillion = ["","Thousand","Million","Billion"]
        res = ''
        M = 1000
        for i in range(len(self.thousandMillionBillion)):
            if num % M != 0:
                res = self.recursion(num%M) + self.thousandMillionBillion[i] + " " + res
            num = num // M
        return res.strip()
    def recursion(self, num):
        if num == 0: return ""
        elif num < 20: return self.lessThan20[num] + " "
        elif num < 100: return self.tens[num//10] + " " + self.recursion(num%10)
        return self.lessThan20[num//100] + ' Hundred ' + self.recursion(num%100)
        