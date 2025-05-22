class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        directions = [(0, -1) , (-1, 0), (1, 0), (0, 1)]
        res = set()
        R = len(board)
        C = len(board[0])
        
        def search_prefix(r, c , node, path,visited):
            if node.flag:
                res.add(path)
                node.flag = False
            
            visited.add((r, c))
            
            for dir_x, dir_y in directions:
                new_r, new_c = r + dir_x , c + dir_y
                if ((0 <= new_r < R) and (0 <= new_c < C)) and ((new_r, new_c) not in visited):
                    new_ch = board[new_r][new_c]
                    if new_ch in node.children:
                        search_prefix(new_r, new_c, node.children[new_ch], path+new_ch, visited)
                        
            visited.remove((r, c))
                        
                    
        def insert(words):
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.flag = True
        insert(words)
        
        
        node = root
        word = ""
        for i in range(R):
            for j in range(C):
                ch = board[i][j]
                if ch in node.children:
                    search_prefix(i , j , node.children[ch], ch, set())
        
        return list(res)