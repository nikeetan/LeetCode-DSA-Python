# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        stack=[]
        for i in lists:
            temp=i  
            while temp:
                stack.append(temp.val)
                temp=temp.next     
        if len(stack)==1:
            newnode=ListNode(stack[0])
            return newnode
        elif len(stack)>1:
            stack=sorted(stack)
            newnode=ListNode(0)
            head=newnode
            for i in range(len(stack)-1):
                newnode.val=stack[i]
                newnode.next=ListNode(0,None)
                newnode=newnode.next
            newnode.val=stack[i+1]
            return head
        else:
            return None
        
