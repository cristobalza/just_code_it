# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(float('inf'), head)
        prev, curr, nxt = dummy, head, head.next
        while nxt:
            if curr.val == nxt.val:
                while curr and nxt and curr.val == nxt.val:
                    curr.next, nxt = nxt.next, nxt.next
                if nxt and nxt.next:
                    prev.next, curr, nxt = nxt, nxt, nxt.next
                else:
                     prev.next, curr, nxt = nxt, nxt, None
            else:
                prev, curr, nxt = curr, nxt, nxt.next
        return dummy.next
        
        
        