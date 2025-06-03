'''
generating all the substring and storing them in a hash_map and then comparing the occ_count which are equal to 3 and among the keys which holds the substring we will check which one is longer
o(n**2) + o(k)

'''
class Solution:
    def maximumLength(self, s: str) -> int:
        d  = collections.defaultdict(int)
        max_string_val = float(-inf)
        for i in range(len(s)):
            curr_sub = []
            for j in range(i, len(s)):
                if not curr_sub or curr_sub[-1] == s[j]:
                    curr_sub.append(s[j])
                    sub_str = ''.join(curr_sub)
                    d[sub_str] += 1
                else:
                    break
        for key, values in d.items():
            if values >= 3:
                if max_string_val < len(key):
                    max_string_val = len(key)
        return max_string_val if max_string_val != float('-inf') else -1



        