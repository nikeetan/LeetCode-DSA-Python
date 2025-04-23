class TrieNode:
    def __init__(self):
        self.children = {}
        self.flag = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        head = TrieNode()
        for curr_dir in folder:
            node = head
            folder = curr_dir.split("/")[1:]
            for sub_folder in folder:
                if sub_folder not in node.children:
                    node.children[sub_folder] = TrieNode()
                node = node.children[sub_folder]
            node.flag = True

        res = []
        path = []
        def dfs(node, path):
            if node.flag:
                res.append("/" + "/".join(path))
                return
            for sub_folder, next_folder in node.children.items():
                dfs(next_folder, path + [sub_folder])
        dfs(head, [])
        return res


            






        # head = TrieNode()
    
        # for path in folder:
        #     node = head
        #     paths = path.split("/")[1:]
        #     print(paths)
        #     for part in paths:
        #         if part not in node.children:
        #             node.children[part] = TrieNode()
        #         node = node.children[part]
        #     node.flag = True
        
        # res = []
        # def dfs(root, folder):
        #     print(folder)
        #     if root.flag:
        #         res.append('/' + '/'.join(folder))
        #         return
        #     for path, child in root.children.items():
        #         print("First",path)
        #         dfs(child, folder + [path])    
        # dfs(head, [])
        # return res




                
