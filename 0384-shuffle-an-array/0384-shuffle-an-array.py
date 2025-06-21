class Solution:

    def __init__(self, nums: List[int]):
        self.array  = nums
        self.arr_cpy = self.array.copy()

    def reset(self) -> List[int]:
        self.array = self.arr_cpy.copy()
        return self.array

    def shuffle(self) -> List[int]:
        last_indx = len(self.array) - 1
        while last_indx > 0:
            shuffle_indx = random.randrange(last_indx + 1)
            self.array[last_indx], self.array[shuffle_indx] = self.array[shuffle_indx], self.array[last_indx]
            last_indx -= 1
        return self.array
                
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()