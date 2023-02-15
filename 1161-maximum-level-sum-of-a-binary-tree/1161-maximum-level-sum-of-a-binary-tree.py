# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        height = 1
        res = (root.val, height) # (sum, height)
        q = collections.deque([root])
        while q:
            curr_sum = 0
            children_num = len(q)
            for _ in range(children_num):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if res[0] < curr_sum:
                res = (curr_sum, height)
            height += 1
        return res[1]
        