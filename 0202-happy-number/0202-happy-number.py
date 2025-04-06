from collections import defaultdict
class Solution:
    def isHappy(self, n: int) -> bool:
        new_number = 0
        hash_numbers = defaultdict(int)
        while (new_number != 1):
            while n != 0:
                remainder = n % 10
                new_number += remainder * remainder
                n = n//10
            if new_number == 1:
                return True
            elif new_number in hash_numbers:
                return False
            else:
                hash_numbers [new_number] = 1
                n = new_number 
                new_number = 0
        return True if new_number == 1 else False