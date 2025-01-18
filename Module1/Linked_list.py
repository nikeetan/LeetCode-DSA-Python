class Node:
    def __init__(self,data):
        self.next=None
        self.val=data

def detect_cycle(head:list[Node])->bool:
    fast,slow=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return True
    return False
        
    

linked_list = Node(5)
head = linked_list
temp = linked_list


temp.next = Node(10)
temp = temp.next
cycle_start = temp  

temp.next = Node(15)
temp = temp.next

temp.next = Node(25)
temp = temp.next

temp.next = Node(30)
temp = temp.next


temp.next = cycle_start
print(detect_cycle(head))