# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums)
    
    def dfs(self, nums):
        if len(nums) == 0:
            return None
        max_val = max(nums)
        idx = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.dfs(nums[:idx])
        root.right = self.dfs(nums[idx+1:])
        return root