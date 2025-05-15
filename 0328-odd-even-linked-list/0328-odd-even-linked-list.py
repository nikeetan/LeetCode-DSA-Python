# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            temp = head
            temp1 = even_head = head.next
            while temp1 and temp1.next:
                temp.next = temp.next.next
                temp = temp.next
                temp1.next = temp1.next.next
                temp1 = temp1.next

            temp.next = even_head
            return head
                
