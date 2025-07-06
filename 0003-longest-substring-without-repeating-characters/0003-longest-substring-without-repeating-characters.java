class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int left = 0, right = 0;
        int windowLength = 0;
        while(right < s.length()){
            if (map.containsKey(s.charAt(right)) && map.get(s.charAt(right)) >= left){
                    left = map.get(s.charAt(right)) + 1;
                }
            map.put(s.charAt(right), right);
            windowLength = Math.max(windowLength, right - left + 1);
            right += 1;
        }
        return windowLength;
    }
    }