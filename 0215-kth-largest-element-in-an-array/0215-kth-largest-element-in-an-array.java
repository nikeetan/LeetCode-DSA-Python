class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new  PriorityQueue<>();
        int result= 0 ; 
        for(int i = 0; i < nums.length; i++){
            maxHeap.add(-1 * nums[i]); 
        }
        for(int i = 0; i<k ; i++){
        result = maxHeap.poll();
        }
        return -1 * result;
    }
}