# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            fetch_len=0
            temp=head
            while temp is not None:
                fetch_len+=1
                temp=temp.next
            k=k%fetch_len     
            slow,fast=head,head
            count=1
            while count<=k:
                if fast.next is None:
                    fast=head
                else:
                    fast=fast.next
                count+=1
            while fast.next:
                slow=slow.next
                fast=fast.next 
            fast.next=head
            head=slow.next
            slow.next=None
            return head

            
        