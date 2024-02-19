from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        new_str=""
        while len(d)!=0:
            k=max(d.values())
            char_app=max(d,key=d.get)
            for i in range(k):
                new_str+=char_app
            d.pop(char_app)
        return new_str
s="tree"
sort_character=Solution()
print(sort_character.frequencySort(s)) 
       