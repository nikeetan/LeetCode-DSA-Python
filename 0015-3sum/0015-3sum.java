class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        HashSet<List<Integer>> res = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if ((i > 0) && (nums[i] == nums[i - 1])){
                continue;
            }
            Set<Integer> seen = new HashSet<>();
            int j = i + 1;
            while(j < nums.length){
                int complement = -nums[i] - nums[j];
                if (seen.contains(complement)){
                    res.add(Arrays.asList(nums[i], nums[j], complement));
                    while(j + 1 < nums.length && nums[j] == nums[j +1]){
                        j += 1;
                    }
                }
                seen.add(nums[j]);
                j += 1;
            } 
        }
        return new ArrayList<>(res);
    }
}


            /*
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
*/