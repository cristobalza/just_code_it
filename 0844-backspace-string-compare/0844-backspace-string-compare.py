class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.check(s) == self.check(t)
    def check(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
        