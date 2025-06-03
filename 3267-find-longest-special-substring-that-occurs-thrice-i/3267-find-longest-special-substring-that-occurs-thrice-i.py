'''
generating all the substring and storing them in a hash_map and then comparing the occ_count which are equal to 3 and among the keys which holds the substring we will check which one is longer
o(n**2) + o(k)

'''
import heapq
class Solution:
    def maximumLength(self, s: str) -> int:
        d  = collections.defaultdict(int)
        max_string_val = float(-inf)
        for i in range(len(s)):
            char = s[i]
            sub_str_len = 0
            for j in range(i, len(s)):
                if char == s[j]:
                    sub_str_len += 1
                    d[(s[j], sub_str_len)] += 1 
                else:
                    break
        for key, val in d.items():
            if val >= 3:
                max_string_val = max(max_string_val, key[-1])
        return max_string_val if max_string_val != float('-inf') else -1
        #return 0
        # for key, values in d.items():
        #     if values >= 3:
