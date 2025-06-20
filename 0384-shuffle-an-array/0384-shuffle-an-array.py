class Solution:

    def __init__(self, nums: List[int]):
        self.array  = nums
        self.arr_cpy = self.array.copy()

    def reset(self) -> List[int]:
        self.array = self.arr_cpy.copy()
        return self.array

    def shuffle(self) -> List[int]:
        temp = self.array.copy()
        for indx in range(len(self.array)):
            popindx = random.randrange(len(temp))
            self.array[indx] = temp.pop(popindx)
        return self.array

                
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()