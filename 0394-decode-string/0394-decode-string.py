class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] != "]":
                stack.append(s[i])
            else:
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                stack.append(k*word)

        return "".join(stack)