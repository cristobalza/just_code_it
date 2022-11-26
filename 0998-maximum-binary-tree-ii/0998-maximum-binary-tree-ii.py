# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        Case 1 the val is greater than any other - just create a new one to left
        Case 2 the val is in between 
        Case 3 the val is at the bottom - beccomes the new leaf node
        '''
        
        self.val = val
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return TreeNode(self.val)

        if node.val < self.val:
            new_node = TreeNode(self.val)
            new_node.left = node
            return new_node

        node.right = self.dfs(node.right)
        # node.left = self.dfs(node.left)
        return node
        
        