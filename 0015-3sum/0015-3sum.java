class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        HashSet<List<Integer>> res = new HashSet<>();
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 2; i++){
            if ((i > 0) && (nums[i] == nums[i - 1])){
                continue;
            }
            int pointer1 = i + 1;
            int pointer2 = nums.length - 1;
            while(pointer1 < pointer2){
                int sum = nums[i] + nums[pointer1] + nums[pointer2];
                if (sum == 0){
                    res.add(Arrays.asList(nums[i], nums[pointer1], nums[pointer2]));
                    while ((pointer1 < pointer2) && (nums[pointer1] == nums[pointer1 + 1])){
                        pointer1 += 1;
                    }
                    while((pointer1 < pointer2) && (nums[pointer2] == nums[pointer2 - 1])){
                        pointer2 -= 1;
                    }
                    pointer1 += 1;
                    pointer2 -= 1;
                }
                else if(sum < 0){
                   pointer1 += 1;
                }
                else{
                      pointer2 -= 1;
                }
            }
        }
        return new ArrayList<>(res);
    }
}