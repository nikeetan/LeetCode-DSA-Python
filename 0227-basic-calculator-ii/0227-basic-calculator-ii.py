'''
3 + 2 * 2
      p

cur_num = 3 
sign = 1 
res = 0

cur_num = 3 
sign = 1 
res = 3

cur_num = 2
sign = 1 
res = 3



'''

class Solution:
    def calculate(self, s: str) -> int:
        curr_num = 0
        sign = '+'
        stk = []
        for ch in range(len(s)):
            if s[ch].isdigit():
                curr_num = curr_num * 10 + int(s[ch])
            if s[ch] in '+-*/' or ch == len(s) - 1:
                if sign in '+-':
                    stk.append(-curr_num) if sign == '-' else stk.append(curr_num)
                elif sign == '*':
                    stk.append(stk.pop() * curr_num)
                elif sign =='/':
                    stk.append(int(stk.pop() / curr_num))
                sign = s[ch]
                curr_num = 0
        print(stk)
        return sum(stk)


            

        


        '''
        # Initialize stack
        res = 0
        last_num = 0
        operation = "+"
        curr_num = 0
        curr_char = ""
        indx = 0
        s = s.replace(" ", "")
        while indx < len(s):
            curr_char = s[indx]

            if curr_char.isdigit():
                curr_num = curr_num * 10 + int(curr_char) # 2
            
            if not curr_char.isdigit() or indx == len(s) - 1:

                if operation == '+':
                    res += last_num             # 3
                    last_num = curr_num

                if operation == '-':
                    res += last_num
                    last_num = -1 * curr_num        # - 2
                
                if operation == '*':                    
                    last_num = last_num * curr_num    # - 4
                
                if operation == '/':
                    last_num = int(last_num / curr_num)

                operation = curr_char  # *
                curr_num = 0           # 0 
            indx += 1
        return res + last_num
        '''


'''
3-2*2
res     = 0         
las_num = 0 
curr_num = 3
curr_char = 3
oper = +

res     = 0 
las_num = 3
curr_num = 0
oper = -

res     = 0
las_num = 3
curr_num = 2
oper = -

res     = 3
las_num = -2
curr_num = 0
oper = *

res     = 3
las_num = - 4
curr_num = 0
oper = *


res + last_num 
'''