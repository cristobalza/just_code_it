class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {
            "(":")" , 
            "{":  "}", 
            "[": "]"
            }
        for char in s:
            if char in bracket_dict.keys():
                stack.append(char)
            else:
                if not stack or bracket_dict.get(stack[-1]) != char:
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False