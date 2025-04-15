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

        if x != y:
            self.parent[x] = y

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        group = DSU(len(s))
        for u , v in pairs:
            group.Union(u , v)

        # Group indices on the basis of parents
        group_dict = defaultdict(list)
        for i in range(len(s)):
            root = group.Find(i)
            group_dict[root].append(i)
        
        res = list(s)

        for indices in group_dict.values():
            chars = [s[i] for i in indices]
            chars.sort()
            for indx, char in zip(sorted(indices), chars):
                res[indx] = char
                
        return ''.join(res)
