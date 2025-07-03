import java.util.*; 
class Solution {
    public char kthCharacter(int k) {
        String word = "a";
        while (word.length() < k)
        {
            String generatedString = "";
            for(int i = 0; i < word.length(); i++)
            {
            
                generatedString += (char) ((int) (word.charAt(i)) + 1);
            }
            word = word + generatedString; 
        }

        return word.charAt(k - 1);

    }
}