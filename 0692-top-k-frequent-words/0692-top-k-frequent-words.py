from collections import Counter
from heapq import heappush, heappop

class TrieNode:
    def __init__(self):
        self.child = {}
        self.flag = False


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        w_bucket = [ None for i in range(len(words) + 1)]
        for word, freq in cnt.items():
            if not w_bucket[freq]:
                w_bucket[freq] = TrieNode()
            
            node = w_bucket[freq]
            for i in word:
                if i not in node.child:
                    node.child[i] = TrieNode()
                node = node.child[i]
            node.flag = True

        res = []

        def dfs(node, word):
            if node.flag:
                res.append(word)
            for nei in sorted(node.child):
                dfs(node.child[nei], word + nei)
        
        # Enumerating from N - 1
        
        for i in range(len(words) , 0, -1):
            if len(res) >= k:
                break
            else:
                if w_bucket[i]:
                    node = w_bucket[i]
                    dfs(node, "")
        return res[:k]
            