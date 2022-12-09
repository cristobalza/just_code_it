# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, maxx = 0, minn = float('inf'))
        return self.res
        
    def dfs(self, node: Optional[TreeNode], maxx:int, minn:int) -> None:
        if not node:
            self.res= max(abs(maxx - minn) , self.res)
            return
        
        maxx = max(maxx, node.val)
        minn = min(minn, node.val)
        
        self.dfs(node.left, maxx, minn)
        self.dfs(node.right, maxx, minn)
        return
    
        