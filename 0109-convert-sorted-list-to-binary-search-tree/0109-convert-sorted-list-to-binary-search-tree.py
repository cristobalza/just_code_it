# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        curr, arr= head, []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        def dfs(arr):
            if len(arr) == 0: return None
            l, r = 0, len(arr)
            m = (l + r) // 2
            node = TreeNode(arr[m])
            node.left = dfs(arr[:m])
            node.right = dfs(arr[m+1:])
            return node
        return dfs(arr)