# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        brute force i can think of stack so the first reversal needs to be done at group len 2
        second at group len 4 t
        '''
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
        group_size = 1
        dummy = ListNode(0, None)
        prev = dummy
        curr = head

        # count the no of nodes
        while curr:
            count = 0
            temp = curr
            while temp is not None and count < group_size:
                temp = temp.next
                count += 1
            

            if count % 2 == 0:
                # revserse logic
                new_head, new_tail = reverse(curr , count)
                prev.next = new_head
                new_tail.next = temp
                prev = new_tail
                curr = temp
            else:
                for _ in range(count):
                    prev = curr
                    curr = curr.next
            group_size += 1
        return head
