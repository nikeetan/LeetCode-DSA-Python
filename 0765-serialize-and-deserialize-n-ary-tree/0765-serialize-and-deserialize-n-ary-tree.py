"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

'''
lvl0 = 1
serialize_list = ['1']
lvl1
queue = [2, 3, 4, 5]
serialize_list = ['1', '2', '3', '4', '5']


'''

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        res = []
        def helper(root):
            if root is None:
                return 
            seriaized_str = str(root.val) + '#' + str(len(root.children))
            res.append(seriaized_str)
            for child in root.children:
                helper(child)
        helper(root)
        return ",".join(res)

        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data) == 0:
            return None
        else:
            data = data.split(',')
            queue = deque(data)
            def dfs():
                node_info = queue.popleft()
                node_info = node_info.split('#')
                node = Node(int(node_info[0]))
                no_of_children = int(node_info[-1])
                for child in range(no_of_children):
                    node.children.append(dfs())
                return node
            return dfs()    
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))