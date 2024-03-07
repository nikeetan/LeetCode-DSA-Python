class ListNode:
    def __init__(self,data,next):
        self.data=data
        self.next=None
    def Insert_List(self,data:int):
        i=0
        newnode=ListNode(0,None)
        head=newnode
        newnode=ListNode(data,None)
        newnode=newnode.next
        return head
    

Link_List=ListNode(0,None)


