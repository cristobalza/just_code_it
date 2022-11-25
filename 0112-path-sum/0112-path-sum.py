# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.targetSum = targetSum
        if root.left and root.right:
            return self.dfs(root.left, root.val) or self.dfs(root.right, root.val)
        elif root.left:
            return self.dfs(root.left, root.val)
        elif root.right:
            return self.dfs(root.right, root.val)
        else:
            return root.val == targetSum
    def dfs(self, node, cummSum):
        if not node.left and not node.right:
            return cummSum + node.val == self.targetSum
        if node.left and node.right:
            return self.dfs(node.left, cummSum + node.val) or self.dfs(node.right, cummSum + node.val)
        elif node.left:
            return self.dfs(node.left, cummSum + node.val)
        else:
            return self.dfs(node.right, cummSum + node.val)
        