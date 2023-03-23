# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, k):
            if not node: return None
            if node.val > k:
                node.left = dfs(node.left, k)
            elif node.val < k:
                node.right = dfs(node.right, k)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    curr = node.left
                    while curr.right:
                        curr = curr.right
                    node.val = curr.val
                    node.left = dfs(node.left, curr.val)
                    
            return node
        return dfs(root, key)
                        
                    
        