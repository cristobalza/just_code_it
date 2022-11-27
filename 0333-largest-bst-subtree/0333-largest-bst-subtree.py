# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_count = 0
        self.dfs(root)
        return self.max_count
    
    def dfs(self, node):
        if not node:
            return
        if self.bst_search(node, float('-inf'), float('inf')):
            self.max_count = max(self.counting(node), self.max_count)
        self.dfs(node.left)
        self.dfs(node.right)
        return
    
    def bst_search(self, node, low, high) :
        if not node:
            return True
        
        if node.val <= low or node.val >= high:
            return False
        
        l = self.bst_search(node.left, low, node.val)
        r = self.bst_search(node.right, node.val, high)
        
        return l and r
    
    def counting(self, node):
        if not node:
            return 0
        return 1 + self.counting(node.left) + self.counting(node.right)
        