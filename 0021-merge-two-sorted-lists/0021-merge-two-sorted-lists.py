# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node1 = list1
        node2 = list2
        if node1 is None and node2 is None:
            return node1
        else:
            head = ListNode(0, None)
            temp = head
            while node1 and node2:
                if node1.val < node2.val:
                    temp.val = node1.val    
                    node1 = node1.next
                else:
                    temp.val = node2.val
                    node2 = node2.next
                
                temp.next = ListNode(0, None)
                temp = temp.next
    
            if node1:
                while node1:
                    temp.val = node1.val
                    node1 = node1.next
                    if node1:
                        temp.next = ListNode(0, None)
                        temp = temp.next
            if node2:
                while node2:
                    temp.val = node2.val
                    node2 = node2.next
                    if node2:
                        temp.next = ListNode(0, None)
                        temp = temp.next
            return head 

