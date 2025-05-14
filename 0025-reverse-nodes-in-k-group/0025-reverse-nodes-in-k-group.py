# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, k):
            prev = None
            curr = start
            while k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                k -= 1
            return prev, start

            # we will use only one group count to distinguish btw odd and even
        count = 0
        dummy = ListNode(0, None)
        prev = dummy 
        curr = head

        # count the no of nodes
        while curr:
            count = 0
            temp = curr
            while temp is not None and count < k:
                temp = temp.next
                count += 1
            if count == k:
                # revserse logic
                new_head, new_tail = reverse(curr , count)
                prev.next = new_head
                new_tail.next = temp
                prev = new_tail
                curr = temp
            else:
                break
        return dummy.next

        