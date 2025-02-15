# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            carry=(head.val*2)//10
            head.val=(head.val*2)%10
            if carry!=0:
                prev=ListNode(carry,head)
                head=prev
            return head
        else:
            prev,curr,curr_next=None,head,head.next
            while curr_next:
                curr.next,prev,curr,curr_next=prev,curr,curr_next,curr_next.next
            curr.next,prev,curr=prev,curr,curr_next
            head=prev
            temp=head
            carry=0
            prev=None
            while temp:
                total = (temp.val * 2) + carry
                temp.val = total % 10
                carry = total // 10
                prev = temp
                temp=temp.next
            if carry!=0:
                prev.next=ListNode(carry,None)
            prev,curr,curr_next=None,head,head.next
            while curr_next:
                curr.next,prev,curr,curr_next=prev,curr,curr_next,curr_next.next
            curr.next,prev,curr=prev,curr,curr_next
            head=prev
        return head