class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def Insert_Front(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    
    def Insert_Back(self,data):
        newnode=Node(data)
        if self.head:
            temp=self.head
            prev=None
            while temp is not None:
                prev=temp
                temp=temp.next
            prev.next =newnode
            newnode.prev = prev
            prev=newnode
        else:
            self.head=newnode
        
    def Display(self):
        temp=self.head
        prev=None
        print("Printing list in forward direction:")
        while temp is not None:
            prev=temp
            print(temp.data,end="->")
            temp=temp.next
        print("\nprinting list in backward direction:")
        while prev is not None:
            print(prev.data,end="->")
            prev=prev.prev
        print("\n")



d=DoubleLinkedList()
d.Insert_Back(30)
d.Insert_Front(10)
d.Insert_Front(20)
d.Insert_Back(40)
d.Insert_Back(50)
d.Display()

        



