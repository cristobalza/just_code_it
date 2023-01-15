# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        get_max_height=lambda node: 1 + max(get_max_height(node.left), get_max_height(node.right)) if node else 0
        def dfs(node):
            if not node: return True
            l_h = get_max_height(node.left)
            r_h = get_max_height(node.right)
            if abs(l_h - r_h) > 1: return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)