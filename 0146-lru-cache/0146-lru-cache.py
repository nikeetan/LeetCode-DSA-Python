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
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.lru = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key)
            return self.lru[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        self.lru[key] = value
        self.lru.move_to_end(key)
        if len(self.lru) > self.capacity:
            self.lru.popitem(last = False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)