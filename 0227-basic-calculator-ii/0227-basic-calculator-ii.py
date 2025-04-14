'''

[2, -22, 33, 44]
44 + 33 + (-22) + 2

'''

class Solution:
    def calculate(self, s: str) -> int:
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


