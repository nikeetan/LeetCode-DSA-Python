class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        left, right = 0, 0
        ans = float('-inf')
        while right < len(s):
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1
            d[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans if ans != float('-inf') else 0


                
#from typing import List

'''
input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

input:  arr = ['x','y','z'], str = "aaaabbbbbbzcyx"

output: "zcyx"

find the substring of
str = 
the substring all chars of arr

str 
char by char and then i find all the characters present in arr
i have found a valid string
{4 : [xyyz]}
valid sub string x y y z  of arr
i = 0 
i = len(str) - len(arr)
0 - 5 # outer loop
inner for loop traverses from i to n
0 -3 x y y z

p1 = 0, p2 = 3 [ 0:  3] {4 : ["xyyz"]}
p1 = x 

[1 :]



'''
'''
from collections import Counter
def get_shortest_unique_substring(arr: List[str], str: str) -> str:
    prev_len = float("inf")
    res = ""
    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            if all(elem in Counter(str[i:j]).keys() for elem in arr):
            # if set(arr) in set(Counter(str[i:j]).keys()):
                if j - i +1 < prev_len:
                    prev_len = j - i +1
                    res = str[i:j]
    #             sub_str_list.append(str[i:j])
    
    # res = sub_str_list[0] if sub_str_list else ""

    # for st in sub_str_list[1:]:
    #     if len(st) < len(res):
    #         res = st

    return res

print(get_shortest_unique_substring(['A','B','C'],'ADOBECODEBANCDDD'))
'''    


