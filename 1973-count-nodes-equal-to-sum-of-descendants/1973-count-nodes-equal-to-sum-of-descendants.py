# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        self.count =0
        self.dfs(root)
        return self.count
    
    def dfs(self, node):
        if not node: 
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        if l + r == node.val:
            self.count += 1
        return l + r + node.val
        