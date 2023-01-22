class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for val in num:
            while stack and stack[-1] > val and k > 0:
                stack.pop()
                k -= 1
            if stack or val != '0':
                stack.append(val)
        stack = stack[:-k] if k else stack
        return "".join(stack).lstrip('0') if stack  else '0'