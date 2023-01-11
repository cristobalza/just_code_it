# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        get_h=lambda node: 1 + max(get_h(node.left), get_h(node.right)) if node else 0
        def dfs(node):
            if not node: return True
            left_h = get_h(node.left)
            right_h = get_h(node.right)
            if abs(left_h - right_h) > 1: return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
                
        