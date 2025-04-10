
class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.is_end = False

    def get(self, ch):
        return self.links[ord('a')-ord(ch)]

    def contains(self, ch):
        return self.links[ord('a')-ord(ch)] is not None
    
    def put(self, ch, node):
        self.links[ord('a') - ord(ch)] = node

    def is_end(self):
        return self.is_end
    
    def set_end(self):
        self.is_end = True


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.contains(ch):
                return False
            node = node.get(ch)
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if node.contains(ch):
                node = node.get(ch)
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)