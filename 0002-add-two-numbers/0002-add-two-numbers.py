# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1=0
        curr=None
        carry=0
        n1=l1
        prev=None
        while l1 and l2:
            sum1=(l1.val+l2.val+carry)
            carry=(sum1//10)
            l1.val=sum1%10
            prev=l1
            l1=l1.next
            l2=l2.next
        if ((l1 is None) and (l2 is None) and carry==0):
            return n1 
        elif ((l1 is None) and (l2 is None) and carry==1):
            prev.next=ListNode(1)
            return n1 
        else:        
            if l2:
                prev.next=l2
            curr=prev.next
            prev=None
            while carry!=0 and curr:
                val1=(curr.val+carry)
                carry=val1//10
                curr.val=val1%10
                prev=curr
                curr=curr.next
            if carry!=0:
                prev.next=ListNode(1)
            return n1
    


      