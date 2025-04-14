'''

[2, -22, 33, 44]
44 + 33 + (-22) + 2

'''

class Solution:
    def calculate(self, s: str) -> int:
        # Initialize stack
        
        stk = []
        operation = "+"
        curr_num = 0
        curr_char = ""
        indx = 0
        s = s.replace(" ", "")
        while indx < len(s):
            curr_char = s[indx]
            if curr_char.isdigit():
                curr_num = curr_num * 10 + int(curr_char)

            if not(curr_char.isdigit()) or indx == len(s) - 1:
                if operation == '+':
                    stk.append(curr_num)
                if operation == '-':
                    stk.append(- curr_num)
                if operation == '*':
                    stk.append(stk.pop() * curr_num)
                if operation == '/':
                    stk.append(int (stk.pop() / curr_num))
                operation = curr_char
                curr_num = 0
            indx += 1
        return sum(stk)
