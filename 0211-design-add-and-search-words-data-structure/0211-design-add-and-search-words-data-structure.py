class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class WordDictionary:

    # def __init__(self):
    #     # TC : O(1)
    #     # SC : O(1)
    #     self.d = defaultdict(set)

    # def addWord(self, word: str) -> None:
    #     # TC : O(1)
    #     # SC : O(n) where n is the number of add operations in the  input
    #     self.d[len(word)].add(word)

    # def search(self, word: str) -> bool:
    #     '''
    #     TC : lets say we have 3 words of same length in that case we will iterate thrice
    #     similarly if we have the n words and each of equal length m in the worst case we will to iterate n times 
    #     each as we said have equal length then the inner loop also runs m times so total time complexity is O(n * m)
    #     SC : O(1)
    #     '''
    #     m = len(word)
    #     for dict_word in self.d[m]:
    #         i = 0
    #         while i < m and (dict_word[i] == word[i] or word[i] == "."):
    #             i += 1
    #         if i == m:
    #             return True
    #     return False
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word : str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.flag = True

    def search(self, word : str):
        '''
        .ab

        root
            abb
            bbb
            cab
            dab
            eda
        '''
        node = self.root
        indx = 0
        def dfs(node, indx):
            if indx == len(word) and node.flag: # satisfies the word len and exists
                return True
            elif indx == len(word) and not(node.flag): # check whether the curr child exceeds more chars
                return False


            if ((word[indx] != '.') and (word[indx] in node.children)): # to traverse to the child node
                return dfs(node.children[word[indx]], indx + 1)
            elif word[indx] == '.': # if '.' Take any neighbour and check
                for child in node.children:
                    if dfs(node.children[child],indx + 1):
                        return True
            else: # check if the word we want to search doesn't exist in the trie node
                return False 
            return False
        return dfs(node, indx)


# Overall TC : O(N2) SC : O(N)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)