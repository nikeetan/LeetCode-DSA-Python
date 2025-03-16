# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev=None
            curr=head
            curr_next=curr.next
            while curr_next is not None:
                curr.next,prev,curr,curr_next=prev,curr,curr_next,curr_next.next
            curr.next=prev
            return curr
        else:
            return head

            