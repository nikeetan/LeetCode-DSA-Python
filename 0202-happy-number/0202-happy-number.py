from collections import defaultdict
class Solution:
    def next_number(self, n):
        new_number = 0
        while n > 0:
            remainder = n % 10
            new_number += remainder**2
            n = n // 10
        return new_number

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.next_number(n)
        while slow != fast and fast != 1:
            slow = self.next_number(slow)
            fast = self.next_number(self.next_number(fast))

        return fast == 1

