class Solution {
    public boolean isValid(String s) {
        Stack <Character> charStack = new Stack<>();
        for (char chars : s.toCharArray()){
            if ((chars == '(') || (chars == '[') || (chars == '{')){
                charStack.push(chars);
            }
            else if ((chars == ')') || (chars == ']') || (chars == '}')){
                if (!charStack.isEmpty())
                {
                    if ((chars == ')') && (charStack.peek() != '(')){
                        return false;
                    }
                    else if ((chars == '}') && (charStack.peek() != '{')){
                        return false;
                    }
                    else if ((chars == ']') && (charStack.peek() != '[')){
                        return false;
                    }
                    charStack.pop();
                }
                else
                {
                    return false;
                }
            }
        }
    if (charStack.isEmpty()){
        return true;
    }
    return false;
    }

}