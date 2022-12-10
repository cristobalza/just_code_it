class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 2:
            return int(tokens[-1])
        stack= []
        # t ='-11'
        # print(t.isdigit())
        # print(t[0]=='-')
        # print(t[1:].isdigit())
        
        for tok in tokens:
            if tok.isdigit() or (tok[0]=='-'and tok[1:].isdigit()):
                stack.append(tok)
                continue
            else:
                if tok == "+":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a+b)
                    
                elif tok == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(b-a)
                
                elif tok == '*':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(a*b)
                    
                elif tok == "/":
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b/a))
        return stack[-1]
                    
        