# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, self.pos2valArr = [], collections.defaultdict(list)
        self.bfs(root)
        min_, max_ = min(self.pos2valArr.keys()), max(self.pos2valArr.keys())
        for i in range(min_, max_ + 1):
            res.append(self.pos2valArr[i])
        return res
    
    def bfs(self, root):
        q = collections.deque([(root, 0)])
        while q:
            node, pos = q.popleft()
            self.pos2valArr[pos].append(node.val)
            if node.left:
                q.append((node.left, pos - 1))
            if node.right:
                q.append((node.right, pos + 1))
        return None