# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Gareeb approach
        take in hash and remove the duplicate values
        '''
        if head:
            temp=head
            d={}
            new_list=ListNode(0)
            head=new_list
            prev=None
            while temp is not None:
                if temp.val not in d:
                    d[temp.val]=1
                    new_list.val=temp.val
                    new_list.next=ListNode(0,None)
                    prev=new_list
                    new_list=new_list.next
                temp=temp.next
            prev.next=None
        return head
        