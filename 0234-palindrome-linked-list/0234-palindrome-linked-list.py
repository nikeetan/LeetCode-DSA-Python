# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
 Naive solution is stack and two pointers and compare the first and the last so that gives me 
 TC : O(N) + O(N/2) ~ O(N)
 SC : O(N)



'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front = head

        def helper(head):
            if head is not None:            
                if not helper(head.next):
                    return False
                if head.val != self.front.val:
                    return False
                self.front = self.front.next
            return True
        return helper(head)
        

        