class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class link_list:
    def __init__(self):
        self.head=None
    
    def Insert_Front(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    
    def Insert_Back(self,data):
        newnode=Node(data)
        prev=None
        temp=self.head
        if self.head:
            while temp is not None:
                prev=temp
                temp=temp.next
            prev.next=newnode
        else:
            self.head=newnode
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next

Single_link_list=link_list()

Single_link_list.Insert_Front(5)
Single_link_list.Insert_Front(10)
Single_link_list.Insert_Back(20)

Single_link_list.display()



        
    
        


