# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        is_null = False
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                is_null = True
                continue
            if is_null: return False
            q.append(node.left)
            q.append(node.right)
        return True
        