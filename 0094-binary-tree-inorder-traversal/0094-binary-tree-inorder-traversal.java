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

    public List<Integer> inorderTraversal(TreeNode root) {
    
        ArrayList<Integer> inorderList = new ArrayList<>();
        Stack<TreeNode> stk = new Stack<>();
        TreeNode curr = root;
        while (!stk.isEmpty() || curr != null)
        {   
            while (curr != null)
            {
                stk.push(curr);
                curr = curr.left;
            }
            curr = stk.pop();
            inorderList.add(curr.val);
            curr = curr.right;
        }
        return inorderList; 

    }
}