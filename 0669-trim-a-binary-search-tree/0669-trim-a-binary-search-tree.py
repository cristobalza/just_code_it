# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low, self.high = low, high
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return None
        if node.val < self.low:
            return self.dfs(node.right)
        if node.val > self.high:
            return self.dfs(node.left)
        # root = TreeNode(node.val)
        node.left = self.dfs(node.left)
        node.right = self.dfs(node.right)
        return node
        