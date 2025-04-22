class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
 
        char_table = [0] * 26

        for i in s:
            char_table[ord(i) - ord('a')] += 1

        for i in t:
            char_table[ord(i) - ord('a')] -= 1 
            if char_table[ord(i) - ord('a')] < 0:
                return False
        return True