from queue import Queue


class Stack:
    '''
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.Sl=[]
    '''

    def print_elements(self,q:Queue,l:list):
        l1=[]
        print("Printing from the Queue:")
        while not(q.empty()):
            print(q.get())
        print("Printing from the stack:")
        while len(l)!=0:
            k=l.pop()
            l1.append(k)
        while len(l1)!=0:
            print(l1.pop())

    def Insert_Element(self):
        q=Queue(4)
        l=[]
        q.put(1)
        q.put(2)
        q.put(3)
        q.put(4)
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        self.print_elements(q,l)

    
new=Stack()
new.Insert_Element()
