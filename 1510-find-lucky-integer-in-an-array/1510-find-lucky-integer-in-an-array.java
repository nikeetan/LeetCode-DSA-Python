class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer, Integer> map = new HashMap <>();
        int maxKey = Integer.MIN_VALUE;
        for (int i = 0; i < arr.length; i ++){
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
        }
        for(int key : map.keySet()){
            if (key == map.get(key)){
                maxKey = Math.max(maxKey, key);
            } 
        }
        if(maxKey != Integer.MIN_VALUE){
            return maxKey;
        }
        return -1;
    }
}