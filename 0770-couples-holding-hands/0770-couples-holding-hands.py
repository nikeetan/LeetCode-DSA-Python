'''
if its even number of positions where in the couples are not seated properly then we will have the swap_count as number of couples not seated properly //2
else number of couples not seated properly - 1
'''

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            self.parent[rootX] = rootY
    
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        seats = len(row) // 2
        header = DSU(seats)
        for i in range(0, len(row), 2):
            header.union(row[i] // 2, row[i + 1] // 2)
        count = 0
        for i , representative in enumerate(header.parent):
            if representative == i:
                count += 1
        return seats - count

        




