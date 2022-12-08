# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = self.dfs(root1, [])
        arr2 = self.dfs(root2, [])
        return arr1 == arr2
    
    def dfs(self, node, subset):
        if not node:
            return subset
        if not node.left and not node.right:
            subset.append(node.val)
            return subset
        self.dfs(node.left,subset)
        self.dfs(node.right, subset)
        return subset
        
        