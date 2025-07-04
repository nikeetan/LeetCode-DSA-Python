/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if ((head == null) || (head.next == null)){
            return head;
        }
        ListNode firstNode = head;
        ListNode secondNode = head.next;
        int temp;
        while (secondNode != null){
            temp = firstNode.val;
            firstNode.val = secondNode.val;
            secondNode.val = temp;
            if (secondNode.next != null){
            firstNode = firstNode.next.next;
            secondNode = firstNode.next;
            }
            else{
                secondNode = secondNode.next;
            }
        }
        return head;
    }
}