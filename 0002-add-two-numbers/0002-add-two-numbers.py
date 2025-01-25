# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2=0,0
        sum1=0
        dh=ListNode(0)
        curr=dh
        carry=0
        while l1 and l2:
            sum1=(l1.val+l2.val+carry)
            carry=(sum1//10)
            newnode=ListNode(sum1%10)
            curr.next=newnode
            curr=curr.next
            l1=l1.next
            l2=l2.next
            
        val1,v1l2=0,0
        while carry!=0:            
            if l1:
                val1=l1.val
                l1=l1.next
            else:
                val1=0
            if l2:
                val2=l2.val
                l2=l2.next
            else:
                val2=0
            sum1=val1+val2+carry
            newnode=ListNode(sum1%10)
            carry=sum1//10
            curr.next=newnode
            curr=curr.next
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        return dh.next
