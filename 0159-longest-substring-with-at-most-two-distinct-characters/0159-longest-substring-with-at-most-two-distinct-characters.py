'''
fix one pointer at the 0th location 
and start the second pointer at the 0th location
when i reach the length of dictionary > 2 i will compute the window size

then i will move the first pointer

'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = float('-inf')
        left, right = 0, 0
        d = collections.defaultdict((int))
        while right < len(s):
            d[s[right]] += 1
            while len(d) > 2 and left < right:
                if d[s[left]] - 1 == 0:
                    del d[s[left]]
                else:
                    d[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans 

        
        # for i in range(len(s)):
        #     d = {}
        #     for j in range(i, len(s)):
        #         d[s[j]] = 1
        #         if len(d) > 2:
        #             break
        #         ans = max(ans, j - i + 1)
        # return ans
        