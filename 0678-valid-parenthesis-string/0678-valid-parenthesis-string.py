class Solution:
    def checkValidString(self, s: str) -> bool:
        leftP, star = collections.deque(), collections.deque()
        for i in range(len(s)):
            if s[i] == '(':
                leftP.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if leftP:
                    leftP.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while leftP:
            idx = leftP.popleft()
            while star and star[0] < idx:
                star.popleft()
            if not star:
                return False
            star.popleft()
        
        return True 
                    