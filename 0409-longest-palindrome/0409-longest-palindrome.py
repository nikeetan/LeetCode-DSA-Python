'''
one approach is like take the permutation of the string and then check which makes the palindrome among them and return the one with maximum length

a = 3 
b = 3
c = 3
'''



class Solution:
    def longestPalindrome(self, s: str) -> int:
       
        frequency_map = {}
       
        for c in s:
            frequency_map[c] = frequency_map.get(c, 0) + 1

        res = 0
        has_odd_frequency = False
        for freq in frequency_map.values():
       
            if (freq % 2) == 0:
                res += freq
            else:
                
                
                res += freq - 1
                has_odd_frequency = True

        if has_odd_frequency:
            return res + 1

        return res