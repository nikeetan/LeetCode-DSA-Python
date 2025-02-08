import heapq
class NumberContainers:

    def __init__(self):
        self.ind={}
        self.numb=defaultdict(list)
    def change(self, index: int, number: int) -> None:
        self.ind[index]=number
        heappush(self.numb[number],index)

    def find(self, number: int) -> int:
        if number not in self.numb:
            return -1
        while self.numb[number]:
            if self.ind[self.numb[number][0]]==number:
                return self.numb[number][0]
            heappop(self.numb[number])
        return -1

        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)