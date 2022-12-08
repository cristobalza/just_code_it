# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.dfs(root, low, high)
        
    def dfs(self, node, low, high):
        if not node or (node.val < low and not node.right) or (node.val > high and not node.left):
            return 0
        if node.val < low:
            return self.dfs(node.right, low, high)
        if node.val > high:
            return self.dfs(node.left, low, high)
        else:
            return node.val + self.dfs(node.left, low, high) + self.dfs(node.right, low, high)
