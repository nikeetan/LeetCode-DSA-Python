import random
class RandomizedSet:

    def __init__(self):
        self.list1=set()

    def insert(self, val: int) -> bool:
        if val in self.list1:
            return False
        self.list1.add(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.list1:
            return False
        self.list1.remove(val)
        return True
        
    def getRandom(self) -> int:
        if self.list1:
            return (random.choices(list(self.list1))[0])
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()