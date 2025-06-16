class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        def is_valid_bst(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return is_valid_bst(node.left, low, node.val) and is_valid_bst(node.right, node.val, high)

        if not trees:
            return None
        if len(trees) == 1:
            return trees[0] if is_valid_bst(trees[0], float('-inf'), float('inf')) else None

        root_map = {tree.val: (tree, i) for i, tree in enumerate(trees)}
        leaf_vals = set()
        for tree in trees:
            if tree.left:
                leaf_vals.add(tree.left.val)
            if tree.right:
                leaf_vals.add(tree.right.val)

        candidates = [tree for tree in trees if tree.val not in leaf_vals]
        if len(candidates) != 1:
            return None
        root = candidates[0]

        used = set()

        def merge(node):
            if not node:
                return None
            if not node.left and not node.right and node.val in root_map and node.val not in used:
                subtree, _ = root_map[node.val]
                used.add(node.val)
                node.left = subtree.left
                node.right = subtree.right
            node.left = merge(node.left)
            node.right = merge(node.right)
            return node

        final_root = merge(root)
        if not is_valid_bst(final_root, float('-inf'), float('inf')):
            return None
        if len(used) != len(trees) - 1:
            return None
        return final_root
