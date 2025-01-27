class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

def Traverse(Head:Node):
    temp=Head
    while temp is not None:
        print(temp.data)
        temp=temp.next


def Second_half(Head:Node):
    temp=Head
    slow=temp
    fast=temp

    while fast and fast.next:
        temp=slow
        slow=slow.next
        fast=fast.next.next    
    prev=None
    curr=slow
    Next=curr.next

    while Next:
        curr.next=prev
        prev=curr
        curr=Next
        Next=Next.next
    curr.next=prev
    prev=curr
    temp.next=curr

    Traverse(Head)

def Rotate_ktime(Head:Node, k:int):
    count=1 
    slow,fast=Head,Head
    while count<=k:
        fast=fast.next
        count+=1
    while fast.next:
        slow=slow.next
        fast=fast.next
    fast.next=Head
    Head=slow.next
    slow.next=None
    Traverse(Head)



def Rev_naive(Head:Node):
    temp=Head
    stack1=[]
    while temp is not None:
        stack1.append(temp.data)
        temp=temp.next
    p1=len(stack1)-1
    newlist=Node(0)
    Head = newlist
    while p1>=0:
        newlist.next=Node(stack1[p1])
        newlist=newlist.next
        p1-=1
    Head=Head.next
    Traverse(Head)

def Rev_optimal(Head:Node):
    curr=Head
    Next=curr.next
    prev=None
    while Next:
        curr.next=prev
        prev=curr
        curr=Next
        Next=Next.next
    curr.next=prev
    prev=curr
    Head=curr
    Traverse(Head)

Head = Node(1)
temp=Head
temp.next=Node(2)
temp=temp.next
temp.next=Node(3)
temp=temp.next
temp.next=Node(4)
temp=temp.next
temp.next=Node(5)


Rotate_ktime(Head,k=3)

#Second_half(Head)

# print("Before Reversing")
# Traverse(Head)
# print("After Reversing Naive Approach")
# Rev_naive(Head)
# print("After Reversing Optimal Approach")
# Rev_optimal(Head)

