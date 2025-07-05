class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        else{
        int charPos [] = new int[26];
        for (char c : s.toCharArray()){
            charPos[(int) c - 97] += 1 ;
        }
        for (char c1 : t.toCharArray()){
            if (charPos[(int) c1 - 97] - 1 < 0){
                return false;
            }
            charPos[(int) c1 - 97] -= 1;
        }
        return true;
        }
    }
}