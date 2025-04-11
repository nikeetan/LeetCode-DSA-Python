# class TrieNode:
#     def __init__(self):
#         self.links = [0] * 26
#         self.is_end = False

#     def put(self, ch, node):
#         self.links[ ord('a') - ord(ch)] = node
    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for j in range(1, len(strs)):
            while strs[j].find(prefix):
                prefix = prefix [ :len(prefix) - 1]
                if len(prefix) == 0:
                    prefix = ""
        return prefix