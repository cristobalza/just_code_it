# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.sum2freq = collections.defaultdict(int)
        self.dfs(root)
        max_freq = max(self.sum2freq.values())
        res = [summ for summ, freq in self.sum2freq.items() if freq == max_freq]
        return res
    
    def dfs(self, node):
        if not node:
            return 0
        summ = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.sum2freq[summ] += 1
        return summ
        
                
        