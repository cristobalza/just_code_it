# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.dfs(root)
        return self.res 
    
    def dfs(self, node):
        if not node:
            return 0
        l = max(self.dfs(node.left), 0)
        r = max(self.dfs(node.right), 0)
        curr = node.val + l + r
        self.res = max(self.res, curr, node.val)
        return node.val + max(l,  r)