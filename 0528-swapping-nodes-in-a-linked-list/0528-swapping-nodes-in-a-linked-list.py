# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            fp = head
            sp = head
            for i in range(k - 1):
                fp = fp.next
            first_swap = fp
            while fp.next is not None:
                fp = fp.next
                sp = sp.next
            first_swap.val , sp.val = sp.val , first_swap.val
        return head