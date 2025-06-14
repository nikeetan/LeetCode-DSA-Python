'''
1000
0100
0099
0000
'''

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        numbers = [num1, num2, num3]
        formatted_numbers = [str(num).zfill(4) for num in numbers]
        curr_indx = 0
        key = 0
        while curr_indx <= 3:
            key = key * 10 + min(int(formatted_numbers[0][curr_indx]),int(formatted_numbers[1][curr_indx]), int(formatted_numbers[2][curr_indx]))
            curr_indx += 1
        return key