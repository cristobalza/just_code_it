# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root, TreeNode(float('inf')))
        return self.count
    def dfs(self, node, prev):
        if not node:
            return True
        l = self.dfs(node.left, node)
        r = self.dfs(node.right, node)
        if l and r:
            self.count += 1
        return l and r and node.val == prev.val
        
    