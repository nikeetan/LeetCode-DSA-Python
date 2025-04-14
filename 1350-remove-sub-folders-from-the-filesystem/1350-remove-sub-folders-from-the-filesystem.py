class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        head = TrieNode()
    
        for path in folder:
            node = head
            paths = path.split("/")[1:]

            for part in paths:
                if part not in node.children:
                    node.children[part] = TrieNode()
                node = node.children[part]
            node.flag = True
        
        res = []
        def dfs(root, folder):
            if root.flag:
                res.append('/' + '/'.join(folder))
                return
            for path, child in root.children.items():
                dfs(child, folder + [path])    
        dfs(head, [])
        return res


                

