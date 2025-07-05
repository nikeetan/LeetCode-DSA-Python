/*
nums = [ 1, 2, 3, 4]
               fp 
                  sp
TC -> O(n**2)
SC -> O(1)
nums = [ 1, 2, 3, 2]
                  cp

map = {1 : 0, 2 : 1, 3 : 2}
return True

TC -> O(n)
SC -> O(n)
*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                return true;
            }
            else{
                map.put(nums[i], i);
            }
        }
        return false;
    }
}

