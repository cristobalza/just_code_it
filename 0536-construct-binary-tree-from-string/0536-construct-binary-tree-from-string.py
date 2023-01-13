# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s: return None
        n = len(s) - 1
        def dfs(i):
            j = i
            while j <= n and (s[j].isdigit() or s[j] == '-'):
                j += 1
            node = TreeNode(int(s[i:j]))
            i = j 
            if i < n and s[i] == "(":
                node.left, i = dfs(i + 1)
                i += 1
            if i < n and s[i] == "(":
                node.right, i = dfs(i + 1)
                i += 1
            return node, i
            
        return dfs(0)[0]
        
        
        