from collections import defaultdict

def group_anagrams(strs):
    l=[]
    fetch_list=[]
    for i in strs:
        d=defaultdict(int)
        for j in i:
            d[j]+=1
        l.append(d)
    for j in l:
        sub_list=[]
        for i,e in enumerate(l):
            if e==j:
                sub_list.append(strs[i])
        if sub_list not in fetch_list:
            fetch_list.append(sub_list)
    return fetch_list
strs=["eattt","tea","tan","ate","nat","bat"]
print(strs)