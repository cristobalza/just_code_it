# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # height-balanced means that the diff between r and l cannot be higher than 1 
        def dfs(arr):
            if len(arr) == 0: return None
            l, r = 0, len(arr)
            m = (l + r) // 2
            node = TreeNode(arr[m])
            node.left = dfs(arr[:m])
            node.right = dfs(arr[m+1:])
            return node
        return dfs(nums)
        