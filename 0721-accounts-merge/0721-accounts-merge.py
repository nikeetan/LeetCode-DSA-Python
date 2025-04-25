class DSU:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
    
    def find_parent(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def Union(self, x , y):
        x = self.find_parent(x)
        y = self.find_parent(y)

        if x != y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x

            elif self.rank[x] < self.rank[y]:
                self.parent[x] = y

            else:
                self.parent[x] = y
                self.rank[y] += 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merge = DSU(len(accounts))
        email_to_name  = {}
        for i in accounts:
            name = i[0]
            base_email = i[1]
            for email in i[1:]:
                # Setting each email as parent of themselves
                merge.add(email)
                # groouping all emails of the account into one base email and then adding the parent that is 0th node of the account to that base_email
                merge.Union(base_email, email)
                email_to_name[email] = name
            #merge.Union(base_email, i[0])
        # group all emails by root parent

        merged_dict = defaultdict(list)
        for email in merge.parent:
            root = merge.find_parent(email)
            merged_dict[root].append(email)
        
        # Now step 3 is converting the emails to account names
        res = []
        for root, emails in merged_dict.items():
            account_name = email_to_name[root]
            res.append([account_name] + sorted(emails))
        return res
