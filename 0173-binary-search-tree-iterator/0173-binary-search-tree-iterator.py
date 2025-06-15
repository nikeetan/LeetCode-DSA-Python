# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.bst = self.helper(root)
        self.pointer = -1
        self.n = len(self.bst)
    def helper(self, root):
        if root is None:
            return []
        left = self.helper(root.left)
        right = self.helper(root.right)
        return left + [root.val] + right

    def next(self) -> int:
        self.pointer += 1
        return self.bst[self.pointer]
    def hasNext(self) -> bool:
        if self.pointer + 1 < self.n:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()