/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 import java.util.*;
class Solution {
    public static int helper(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }
        return 1 + Math.max(helper(root.left),  helper(root.right));
    }
    public int maxDepth(TreeNode root) {
        int depth = 0;
        depth = helper(root);
        return depth;
        
    }
}