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
class Solution {
    public static boolean validCheck(TreeNode root, long leftbound, long rightbound)
    {
        
        if (root == null)
        {
            return true;
        }
        else if ((root.val >= rightbound) || (root.val <= leftbound))
        {
            return false;
        }
        return (validCheck(root.left, leftbound, root.val) && validCheck(root.right, root.val, rightbound));
    }
    public boolean isValidBST(TreeNode root) {
        long leftbound = Long.MIN_VALUE;
        long rightbound = Long.MAX_VALUE;
        return validCheck(root, leftbound, rightbound);
        
    }
}