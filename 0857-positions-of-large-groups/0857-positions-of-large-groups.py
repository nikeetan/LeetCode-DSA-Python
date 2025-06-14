'''
sliding window
append to the res if the length >= 3 
'''

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l, r = 0, 0
        res = []
        while r < len(s):
            if s[l] != s[r]:
                if (r - l) >= 3:
                    res.append([l, r - 1])
                l = r
            r += 1
        if r - l >= 3:
            res.append([l, r - 1])
        return res

'''
test case
                          l
a b c d d d e e e e a  a  b  b  b  c  d
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
                                   r
'''





