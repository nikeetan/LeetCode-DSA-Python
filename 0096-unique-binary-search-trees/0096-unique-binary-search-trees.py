class Solution:
    def numTrees(self, n: int) -> int:
        c = 1
        for i in range(1, n):
            c = (2 * (2 * i + 1) / (i + 2)) * c 
        return int(c)
