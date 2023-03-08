'''Given s: String with ( ) and lowecases
    R: a string with removed invalid pair of ()s  -> in other words, string should have valid parenthesis and return a valid string
    
    only care about the parenthesis
    
    
         0123456
    s = "a)b(c)d"
               i
         
    res = 'ab(c)d'
          
        
         
STACK =[ ]

    for i in range(n)
        stack <- (open or close parenthesis, index)
        
    for i in range(n)
        if s[i] is letter or (stack and i == stack[-1][1])
            output += stack[-1][0]
            stack.pop()
            
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n, q, res = len(s), collections.deque(), ""        
        for i in range(n):
            if s[i] == "(":
                q.append(("(", i))
            elif s[i] == ')':
                if q:
                    if q[-1][0] == '(':
                        q.pop()
                    else:
                        q.append((")", i))
                else:
                    q.append((")", i))
        # print(stack)
        for i in range(n):
            if s[i].isalnum():
                res += s[i]
            else:
                if s[i] != '(' or s[i] != ')':
                    if q and q[0][1] == i:
                        q.popleft()
                        continue
                    res += s[i]
        return res
        