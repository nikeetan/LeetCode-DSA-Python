class Solution:
    def calculate(self, s: str) -> int:

        '''
        lets work on how can i solve 
        5 + 5 * 2 * 10 + 5
              cp
        curr_num = 5
        sign = 1
        res = curr_num * sign + res = 5

        curr_num = 5
        sign = 1

        *
        [5 +]
        res = 5
        sign = *
        curr_num = 0

        curr_num = 2
        sign = *

        curr_num = 2 
        sign = * 
        res = res * curr_num = 10



        3 + 2 * 2
        3 cases
        '''
        context_stack = []
        curr_num = 0
        stk = []
        res = 0
        sign = "+"
        for ch in range(len(s)):
            if s[ch].isdigit():
                curr_num = curr_num * 10 + int(s[ch])
            if s[ch] == '(':
                # Push current context (stack so far + sign)
                context_stack.append((stk, sign))
                stk = []
                sign = '+'
                curr_num = 0

            if (s[ch] in '+-/*') or (ch == len(s) - 1) or s[ch] == ')':
                if sign in '+-':
                    stk.append(curr_num * (1 if sign == "+" else -1))

                elif sign == '*':
                    stk.append(stk.pop() * curr_num)
                    
                elif sign == '/':
                    res = stk.pop()
                    res = int (res / curr_num)
                    stk.append(res)

                sign = s[ch]
                curr_num = 0

            if s[ch] == ')':
                subtotal = sum(stk)
                stk, prev_sign = context_stack.pop()

                if prev_sign == '+':
                    stk.append(subtotal)
                elif prev_sign == '-':
                    stk.append(-subtotal)
                elif prev_sign == '*':
                    stk.append(stk.pop() * subtotal)
                elif prev_sign == '/':
                    stk.append(int(stk.pop() / subtotal))
        return sum(stk)
    



