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
    public void helper(TreeNode root, ArrayList inorderList)
    {
        if (root == null)
        {
            return;
        }
        helper(root.left, inorderList);
        inorderList.add(root.val);
        helper(root.right, inorderList);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> inorderList = new ArrayList<>();
        helper(root, inorderList);
        return inorderList;
    }
}