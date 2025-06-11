'''
monotonic [4, 3, 2, 1] decrease
min heap works
'''


class Solution:
    def clearStars(self, s: str) -> str:
        min_heap = []
        to_remove = {}
        new_string = ""
        for indx, val in enumerate(s):
            if val == '*':
                _, char_indx = heapq.heappop(min_heap)
                to_remove[-1 * char_indx] = 1 
            else:
                heapq.heappush(min_heap, (val, -1 * indx))
        for indx, val in enumerate(s):
            if (val == '*') or (indx in to_remove):
                continue
            new_string += s[indx]
        return new_string
            
        