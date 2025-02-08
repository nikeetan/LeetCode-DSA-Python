class NumberContainers:

    def __init__(self):
        self.ind={}
        self.numb=collections.defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index not in self.ind:
            self.ind[index]=number
        else:
            prev_numb=self.ind[index]
            self.ind[index]=number
            if len(self.numb[prev_numb])==1:
                del self.numb[prev_numb]
            else:
                self.numb[prev_numb].remove(index)
        self.numb[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numb:
            return -1
        else:
            return self.numb[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)