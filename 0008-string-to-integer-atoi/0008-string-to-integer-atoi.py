class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        digit = 0
        digit_cnt = 0
        for i in s:
            if i == ' ' and digit_cnt == 0 and sign == 0:
                continue
            elif i == ' ' and (digit_cnt > 0 or sign != 0):
                break
            elif (ord(i) >= 48) and (ord(i) <= 57):
                digit = digit * 10 + int(i)
                digit_cnt += 1
            elif (i == '-' or i == '+') and (sign == 0) and (digit == 0) and (digit_cnt == 0):
                if i == '-':
                    sign = -1
                else:
                    sign = 1
            elif (i == '-' or i == '+') and ((sign != 0) or (digit_cnt > 0)):
                break
            elif ((ord(i) < 48) or (ord(i) > 57)):
                break
           
        if sign != 0:
            ans = sign * digit
        else:
            ans = digit
        if ans < -1 *(2 ** 31):
            ans = -1 *(2 ** 31)
        elif ans > (2 ** 31) - 1:
            ans = (2 ** 31) - 1
        return ans
        
            

        21474836460
        2147483648
    