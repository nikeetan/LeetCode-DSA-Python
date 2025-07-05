/*
Once i have a maximum occurance of different number than previous i can think of shrinking the window 

*/
import java.util.*;
class Solution {
    public int findShortestSubArray(int[] nums) {
        HashMap<Integer, Integer> count = new HashMap<>();
        HashMap<Integer, Integer> left = new HashMap<>();
        HashMap<Integer, Integer> right = new HashMap<>();


        for(int i = 0; i < nums.length; i ++){
            if (!left.containsKey(nums[i])){
                left.put(nums[i], i);
            }
            if (!right.containsKey(nums[i])){
                right.put(nums[i], i);
            }
            else{
                right.put(nums[i], i);
            }
            count.put(nums[i], count.getOrDefault(nums[i], 0) + 1 );
        }
        int maxOccurance = Collections.max(count.values());
        int length = Integer.MAX_VALUE;
        for (int key : count.keySet())
        {
            if (count.get(key) == maxOccurance){
                length = Math.min(length, (right.get(key) - left.get(key) + 1));
            }
        }
    return length;
    }
}