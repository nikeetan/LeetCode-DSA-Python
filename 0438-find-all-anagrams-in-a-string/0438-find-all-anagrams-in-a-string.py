from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        char_hash = {}
        res = []
        s_map = defaultdict(int)
        for i in range(len(p)):
            if p[i] not in char_hash:
                char_hash[p[i]] = 1
            else:
                char_hash[p[i]] += 1
            if s[i] not in s_map:
                s_map[s[i]] = 1
            else: 
                s_map[s[i]] += 1
        if char_hash == s_map:
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            if s[r] not in s_map:
                s_map[s[r]]  = 1
            else:
                s_map[s[r]]  += 1

            if s_map[s[l]] - 1 == 0:
                del s_map[s[l]]
            else:
                s_map[s[l]] -= 1
            l += 1
            if s_map == char_hash:
                res.append(l)
        return res
        
        
        