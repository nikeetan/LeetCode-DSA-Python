/*
(1)+((2))+(((3)))

maxDepth = 3;
*/


class Solution {
    public int maxDepth(String s) {
        int maxDepth = 0;
        Stack <Character> stack = new Stack<>();
        int depth = 0;
        for (int i = 0; i < s.length(); i ++){
            if (s.charAt(i) == '('){
                depth += 1;
                stack.push('(');
            }
            else if ((!stack.isEmpty()) && (s.charAt(i) == ')')){
                if (depth > maxDepth){
                    maxDepth = Math.max(maxDepth, depth);
                }
                depth -= 1;
                stack.pop(); 
            }
        }
        return maxDepth;
    }
}