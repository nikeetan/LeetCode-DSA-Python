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
            cnt = 1
            fp = head
            sp = None
            first_node = None
            while fp is not None:
                if sp is not None:
                    sp = sp.next
                if cnt == k:
                    first_node = fp
                    sp = head
                cnt += 1
                fp = fp.next
            if sp:
                first_node.val, sp.val = sp.val, first_node.val
            return head