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
        temp = head
        curr_size = 0
        odd_gp = 1
        even_gp = 2
        stk = []
        
        while temp is not None:
            stk.append(temp.val)
            curr_size += 1
            if curr_size == odd_gp:
                curr_size = 0
                odd_gp += 2
            elif curr_size == even_gp:
                start_p = len(stk) - even_gp
                end_p = len(stk) - 1
                while start_p < end_p:
                    stk[start_p], stk[end_p] = stk[end_p], stk[start_p]
                    start_p += 1
                    end_p -= 1
                curr_size = 0
                even_gp += 2
            
            temp = temp.next
        if curr_size > 0 and curr_size % 2 == 0:
            start_p, end_p = len(stk) - curr_size, len(stk) - 1
            while start_p < end_p:
                stk[start_p], stk[end_p] = stk[end_p], stk[start_p]
                start_p += 1
                end_p -= 1
        
        temp = ListNode(None)
        head = temp
        for i in range(len(stk)):
            temp.val = stk[i]
            if i + 1 != len(stk):
                temp.next = ListNode(0, None)
                temp = temp.next
        return head
