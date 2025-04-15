class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]

    def Find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]
    
    def Union(self, x, y):
        x = self.Find(x)
        y = self.Find(y)

        if x == y:
            return False

        if x != y:
            self.parent[x] = y
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs)
        merge = DSU(n)
        comp = n
        for timestamp, u, v in logs:
            if merge.Union(u, v):
                comp -= 1
            if comp == 1:
                return timestamp
        return -1