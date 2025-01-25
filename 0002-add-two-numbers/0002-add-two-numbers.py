# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1,val2=0,0
        colsum=0
        carry=0
        head=ListNode(0)
        curr=head
        while l1 or l2 or carry!=0:
            if l1:
                val1=l1.val
            else:
                val1=0
            if l2:
                val2=l2.val
            else:
                val2=0
            colsum=val1+val2+carry
            carry=colsum//10
            newnode=ListNode(colsum%10)
            curr.next=newnode
            curr=newnode
            if l1:
                l1=l1.next
            else:
                None
            if l2:
                l2=l2.next
            else:
                None
        return head.next

