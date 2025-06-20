class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num_map = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        if len(num2) < len(num1):
            num1, num2 = num2, num1
        # lesser is num1 and greater num2
        num2_indx = len(num2) - 1
        num1_indx = len(num1) - 1
        carry = 0
        result = ""
        
        while num1_indx >= 0:
            digit_sum = num_map[num1[num1_indx]] + num_map[num2[num2_indx]] + carry
            carry = 0 
            if digit_sum >= 10:
                carry = digit_sum // 10
                digit_sum = digit_sum % 10
            result = str(digit_sum) + result
            num1_indx -= 1
            num2_indx -= 1

        while num2_indx >= 0:
            digit_sum = num_map[num2[num2_indx]] + carry
            carry = 0
            if digit_sum >= 10:
                carry = digit_sum // 10
                digit_sum = digit_sum % 10
            result = str(digit_sum) + result
            num2_indx -= 1
        if carry > 0:
            result = str(carry) + result
        return result
            

