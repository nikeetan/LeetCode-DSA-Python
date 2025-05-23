'''
I will do a dfs and then back track when i have the find the cycle
'''

class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find_parent(self, x):
        if self.parent[x] != x:
            x = self.find_parent(self.parent[x])
        return x
    def union(self, x, y):
        x = self.find_parent(x)
        y = self.find_parent(y)

        if x == y:
            return True
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else: 
            self.parent[x] = y
            self.rank[y] += 1 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connect = DSU(len(edges))
        for u, v in edges:
            if connect.union(u, v):
                return [u, v]
        return -1