# class TrieNode:
#     def __init__(self):
#         self.links = [0] * 26
#         self.is_end = False

#     def put(self, ch, node):
#         self.links[ ord('a') - ord(ch)] = node

class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False    

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # '''
        # Brute force would be
        # sort it lexiographically
        # '''
        # strs.sort() # O(logn) n is the number of strings in the lists (o (n * L logn n))
        # p1, p2 = 0, len(strs) - 1
        # indx = 0
        # prefix = ""
        # # incase of equal characters we will be having the o(L) + o(n * L logn)
        # while (indx < len(strs[p1]) and indx < len(strs[p2])) and strs[p1][indx] == strs[p2][indx]:
        #     prefix += strs[p1][indx]
        #     indx += 1
        # return prefix
        # # Space complexity o(L) ["aaa", "aaa", "aaa", "aaa"]

        def insert(root : TrieNode, word : str):
            for char in word:
                if char not in root.children:
                    root.children[char] = TrieNode()
                root = root.children[char]
            root.flag = True

        def common_prefix(root):
            prefix = ""
            while root and len(root.children) == 1 and not root.flag:
                for key, val in root.children.items():
                    char = key
                prefix += char
                root = root.children[char]
            return prefix
            
            
        
        root = TrieNode()
        for word in strs:
            insert(root, word)

        return common_prefix(root)
        
        #TC = O(N * L)
        # SC = O(1)
        







