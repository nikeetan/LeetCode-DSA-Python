
class Solution {
    public String longestCommonPrefix(String[] strs) {
        // Base condition
        if(strs.length == 0 || strs == null) return "";
        
        Arrays.sort(strs);
        String first_word = strs[0];
        String last_word = strs[strs.length-1];
        if (last_word.length() == 0 || first_word.length() == 0) return ""; 
        String prefix =  "";
        String temp = "";
        int i = 0;
        while (i < first_word.length()  && i < last_word.length())
        {
            if (first_word.charAt(i) != last_word.charAt(i))
            {
               break;
            }
            else
            {
               prefix += first_word.charAt(i);
            }
            i += 1;
        }
    return prefix;
    }
    
}