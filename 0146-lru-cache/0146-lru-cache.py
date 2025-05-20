'''
capacity is always positive and also might be 0 ?
How big the capacity can be ?
hash_map get fetches in o(1)
so lets say we get the key value we will swap that with the first 

cap = 2    
ele = [1, 2]
get(1)
ele = [1 , 2]
get(2)
ele = [2, 1]
put(3)
the least will be 1 and when i pop that i will take o(1) 
and when i insert i insert at the 0th position so put takes o(1)

'''


# class OrderedDict:
#     def __init__(self):
#         self.store = {}
#         self.order = []
    
#     def move_to_end(self, key):
#         if key not in self.order:
#             return -1
#         else:
#             self.order.remove(key)
#             self.order.append(key)
            
#     def popitem(self, last):
#         if last:
#             key = self.order.pop()
#         else:
#             key = self.order.pop(0)
#         self.store.pop(key)
    
#     def __len__ (self):
#         return len(self.store)
    
#     def __contains__ (self, key):
#         return key in self.store

#     def __getitem__(self, key):
#         if key in self.store:
#             return self.store[key]
#         else:
#             return -1
    
#     def __setitem__(self, key, value):
#         if key not in self.store:
#             self.order.append(key)
#         self.store[key] = value
class ListNode:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}
       
    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            del self.dic[key]
            self.remove(node)
            self.add(node.key, node.val)
            return node.val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.add(key, value)
        if  len(self.dic) > self.capacity:
            # we should remove the least recent use
            node = self.head.next
            self.remove(node)
            del self.dic[node.key]
           
    
    def add(self, key, value):
        node = ListNode(key, value)
        self.dic[key] = node
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)