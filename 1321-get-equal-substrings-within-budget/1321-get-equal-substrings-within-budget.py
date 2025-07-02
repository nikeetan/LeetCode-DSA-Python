'''
sliding window approach to compute the differene it is O(n) then to fetch the longest substring it is O(n)
two pointers and then calculate the difference if the difference is greater than the maxCost then move ahead
else 
      0  1  2
dp = [2, 1, 1, 1]
         l
               r
maxCost  = 0
lenth = 3
The problem is like when my maximum cost ends and my length of the substring is maximum
TC - > O(n)
SC - > O(1)
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if len(s) == 1 and maxCost == 0: 
            return 0
        else:
            replacements = [0] * len(s)
            curr_indx = 0
            left, right, replace_cost, substrlen = 0, 0, 0, 0
            while curr_indx < len(s):
                replacements[curr_indx] = abs(ord(s[curr_indx]) - ord(t[curr_indx]))
                curr_indx += 1
        
            
            while right < len(s):
            
                replace_cost += replacements[right]
                if replace_cost <= maxCost:
                    substrlen = max(substrlen, right - left + 1)
                else:
                    while left <= right and replace_cost > maxCost:
                        replace_cost -= replacements[left]
                        left += 1
                    substrlen = max(substrlen, right - left + 1)            
                right += 1
            return substrlen




            
            