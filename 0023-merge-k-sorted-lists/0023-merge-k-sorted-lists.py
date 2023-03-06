# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for head in lists:
            curr = head
            while curr:
                heapq.heappush(minheap, curr.val)
                curr = curr.next
        dummy = ListNode(-1, None)
        head = dummy
        while minheap:
            node = ListNode(heapq.heappop(minheap))
            head.next = node
            head = head.next
        return dummy.next
            
        