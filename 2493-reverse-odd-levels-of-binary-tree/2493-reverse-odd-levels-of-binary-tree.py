# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        odd_level = False
        elements = []
        while queue:
            levelElements = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levelElements.append(node.val)
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
            if odd_level:
                levelElements = levelElements[::-1]
                odd_level = False
                elements.extend(levelElements)
                continue
            odd_level = True
            elements.extend(levelElements)
    
       
        #cnstruct binary tree is bascially dfs
        newroot = TreeNode(0)
        def constructBinary(indx : int):
            if indx >= len(elements):
                return None
            newroot = TreeNode(elements[indx])
            newroot.left = constructBinary(2 * indx + 1)
            newroot.right = constructBinary(2 * indx + 2)
            return newroot
        return constructBinary(0)

