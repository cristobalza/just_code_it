# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        # bfs
        q = collections.deque([root])
        res=[]
        while q:
            last_node_idx = len(q) - 1
            for i in range(len(q)):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
                if i == last_node_idx: 
                    res.append(node.val)
        return res