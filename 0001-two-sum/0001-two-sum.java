import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap <Integer, Integer> complementmap = new HashMap <>();
        int complement = 0;
        for(int i = 0; i < nums.length; i ++)
        {
            complement = target - nums[i];
            if (complementmap.containsKey(complement))
            {
               return new int [] {complementmap.get(complement), i};
            }
            else
            {
                complementmap.put(nums[i], i);
            }
        } 

        return new int [0];
    }

}