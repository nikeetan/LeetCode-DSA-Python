'''
monotonic [4, 3, 2, 1] decrease
min heap works
k = count('*')
TC : O(n) + O((n -  k)log(n - k)) 
'''


class Solution:
    def clearStars(self, s: str) -> str:
        min_heap = []
        s = list(s)
        for indx, val in enumerate(s):
            if val == '*' and min_heap:
                _, char_indx = heapq.heappop(min_heap)
                s[-1 * char_indx] = ''
                s[indx] = ''
            else:
                heapq.heappush(min_heap, (val, -1 * indx))
        return ''.join(s)
