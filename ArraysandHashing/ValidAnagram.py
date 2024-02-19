def valid_anagram(s,t):
    k=set(s)
    #k1=set(t)
    k=set(s)
    if len(s)!=len(t):
        return False
    for i in k:
        if s.count(i)!=t.count(i):
            return False
    return True
    

s="anagram"
t="nagaram"
print(valid_anagram(s,t))
