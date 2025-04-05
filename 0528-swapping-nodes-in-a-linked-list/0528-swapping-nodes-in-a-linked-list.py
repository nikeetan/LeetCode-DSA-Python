# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        else:
            temp = head
            length = 0
            while temp is not None:
                length += 1
                temp = temp.next
            indx = k - 1
            curr_cnt = 0
            end_indx = length - k
            temp = head
            first_pointer , second_pointer = None , None
            temp = head
            while temp is not None:
                if curr_cnt == indx:
                    first_pointer = temp
                if curr_cnt == end_indx:
                    second_pointer = temp
                temp = temp.next
                curr_cnt += 1
            first_pointer.val, second_pointer.val = second_pointer.val, first_pointer.val
        return head