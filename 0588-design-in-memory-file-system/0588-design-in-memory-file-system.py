class TrieNode:
    def __init__(self):
        self.folders = {}
        self.content = ""
        self.flag = False

class FileSystem:

    def __init__(self):
        self.fs = TrieNode()
        self.root = self.fs


    def ls(self, path: str) -> List[str]:
        '''
        I should traverse through the path and return the content
        '''
        node = self.root
      
        if path == "/":
            return sorted(list(node.folders.keys()))

        path = path.split("/")[1:]
        for part in path:
            if part in node.folders:
                node = node.folders[part]
            else:
                return []  # Path does not exist
        
        if node.flag:
            return [path[-1]]
        return sorted(node.folders.keys())

    def mkdir(self, path: str) -> None:
        '''
        create a directory
        '''
        path = path.split("/")[1:]
        node = self.root
    
        for paths in path:
            if paths not in node.folders:
                node.folders[paths] = TrieNode()
                #node.folders.move_to_end(paths, last = False)               
            node = node.folders[paths]



    def addContentToFile(self, filePath: str, content: str) -> None:
        path_to_add = filePath.split("/")[1:]
        node = self.root
        for path in path_to_add:
            if path in node.folders:
                node = node.folders[path]
            else:
                node.folders[path] = TrieNode()
                node = node.folders[path]
        node.flag = True
        node.content += content
       
        
      
    def readContentFromFile(self, filePath: str) -> str:
        path_to_read = filePath.split("/")[1:]
        folder = self.root
        for path in path_to_read:
            if path in folder.folders:
                folder = folder.folders[path]
            else:
                return ""
        
        return folder.content

            
       
       


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)