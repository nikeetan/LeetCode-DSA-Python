from collections import defaultdict

class LRUCache:

    def __init__(self, capacity: int):
        self.lru=defaultdict(int)
        self.to_remove=[]
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        else:
            self.to_remove.remove(key)
            self.to_remove.insert(0,key)
            return self.lru[key]


    def put(self, key: int, value: int) -> None:
       
        if len(self.lru)==self.capacity and key not in self.lru:
            k=self.to_remove.pop()
            del(self.lru[k])
        elif key in self.to_remove:
            self.to_remove.remove(key)
        self.to_remove.insert(0,key)
        self.lru[key]=value



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)