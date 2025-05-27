class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find_parent(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def find_union(self, x , y):
        x = self.find_parent(x)
        y = self.find_parent(y)

        if x == y:
            return True
        elif x != y and self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif x != y and self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1 
            

class Solution:
    
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        # Build Graph
        connected_comp = DSU(n)
        for i in range(n - 1):
            if abs (nums[i] - nums[i + 1]) <= maxDiff:
                    connected_comp.find_union(i, i + 1)
        res = []
        for query in queries:
            u, v = query
            if connected_comp.find_parent(u) == connected_comp.find_parent(v):
                res.append(True)
            else:
                res.append(False)  
        return res
          