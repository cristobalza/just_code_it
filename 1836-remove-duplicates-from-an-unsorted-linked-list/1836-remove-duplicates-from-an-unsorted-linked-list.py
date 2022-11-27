# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        val2freq = collections.defaultdict(int)
        dummy = ListNode(float('inf'), head)
        prev, curr = dummy, head
        while curr:
            val2freq[curr.val] += 1
            prev, curr = curr, curr.next
        prev, curr = dummy, head
        while curr:
            if val2freq[curr.val] > 1:
                prev.next, curr = curr.next, curr.next
            else:
                prev, curr = curr, curr.next
        return dummy.next
        
        