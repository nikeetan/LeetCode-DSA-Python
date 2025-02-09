# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr,curr_next=head,head.next
            while curr_next:
                while curr_next and curr_next.val==curr.val:
                    curr_next=curr_next.next
                curr.next=curr_next
                curr=curr_next
                if curr_next:
                    curr_next=curr_next.next
        return head
        