# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp, temp1 = l1, l2
        #You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        n = l1
        carry = 0
        # Traversing until both of them are equal
        prev = None
        while temp  and temp1:
            curr_sum = temp.val + temp1.val + carry
            carry = curr_sum // 10
            temp.val = curr_sum % 10 
            prev = temp
            temp = temp.next
            temp1 = temp1.next
        
        # I check which is the smaller one and i should continue to move with the one which is bigger
        if (temp is None and temp1 is None) and (carry == 0):
            return n
        elif (temp is None and temp1 is None) and (carry > 0):
            prev.next = ListNode(carry)
            return n
        else:
            if temp1:
                prev.next = temp1
            temp = prev.next  
            while temp:
                curr_sum = temp.val + carry
                carry = curr_sum // 10
                temp.val = curr_sum % 10
                prev = temp
                temp = temp.next
        if carry > 0:
            prev.next = ListNode(carry)
        return n