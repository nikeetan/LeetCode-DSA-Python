import random
class RandomizedSet:

    def __init__(self):
        self.hash_map={}
        self.list1=[]

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
       
        self.hash_map[val]=len(self.hash_map)
        self.list1.append(val)
        
        return True
    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        index=self.hash_map[val]
        ele=self.list1[-1]
        self.list1[-1]=val
        self.list1[index]=ele
        self.hash_map[ele]=index
        self.list1.pop()
        del self.hash_map[val]
        return True
        
    def getRandom(self) -> int:
        if self.list1:
            return (random.choices(self.list1)[0])
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()