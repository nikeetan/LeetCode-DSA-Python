# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
using two pointer i will first place the first value then the last and increment first and simiularly the last pointer so for this we will have to maintain a new array  
#Traversal : 
# TC : O(N) + O(N/2) + O(N) ~ O(N)
# SC : O(N) + O(N)
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse
        prev = None
        curr = slow
        while curr is not None:
            curr.next, prev, curr = prev, curr, curr.next
        slow = prev
        # attaching
        # 1 - > 2 - > 3 - > 4 - > 5 
        # 1 - > 2 - > 5 - > 4 - > 3
        '''
                d.    S.    s
        # 1 - > 5 - > 2 - > 4 - > 3

        '''
        first = head
        second = slow
        while second.next:
            first.next, second.next, first, second = second, first.next, first.next, second.next
        
