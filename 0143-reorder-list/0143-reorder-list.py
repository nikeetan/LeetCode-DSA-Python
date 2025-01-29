# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    find middle
    '''
    def reorderList(self,head):
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        prev=None
        curr=slow
        while curr:
            curr.next,prev,curr=prev,curr,curr.next
        first,second=head,prev
        while second.next:
            first.next,first=second,first.next
            second.next,second=first,second.next
        return head
    



    