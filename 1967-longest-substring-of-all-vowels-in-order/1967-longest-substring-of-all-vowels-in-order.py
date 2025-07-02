'''
{'e' : 'a', 'i' : 'e', 'o' : 'e', 'u' : 'o'}
length of the hash_map is 5 what i will do i will expand the window if my next occuring character is 'u'
in between if the order is not followed clear the hashmap and move the left pointer

'''
from collections import defaultdict

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        order_map = {'e' : 'a', 'i' : 'e', 'o' : 'i', 'u' : 'o'}
        vowelCnt = defaultdict(int)
        l, r = 0, 0
        substrLen = 0
        while r < len(word):
            if len(vowelCnt) == 5 and word[r] != 'u':
                vowelCnt = defaultdict(int)
                l = r
            if word[r] == 'a' and len(vowelCnt) <= 1:
                vowelCnt[word[r]] += 1
            elif word[r] == 'a' and len(vowelCnt) > 1:
                vowelCnt = defaultdict(int)
                vowelCnt[word[r]] += 1
                l = r
            else:
                if order_map[word[r]] not in vowelCnt:
                    vowelCnt = defaultdict(int)
                    l = r + 1
                elif word[r] in vowelCnt and word[r - 1] != word[r]:
                    vowelCnt = defaultdict(int)
                    l = r + 1
                else:
                    vowelCnt[word[r]] += 1
            if len(vowelCnt) == 5:
                substrLen = max(substrLen, r - l + 1)
            r += 1
        return substrLen
    