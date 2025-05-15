# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
if the nodes are unique i can think of keeping a hash_map and then everytime i traverse i will keep check if the curr value is the new value or the old value if there is a point where i am at the node whose value is already seen then i will return true
TC : O(N) SC : O(1)

fast and slow pointer fast travers two and slow traverse one

[3,2,0,-4]
 s         
 f       
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        else:
            slow = head
            fast = head.next 
            while slow != fast:
                if ((not fast) or (not fast.next)):
                    return False
                slow = slow.next
                fast = fast.next.next
            return True 
