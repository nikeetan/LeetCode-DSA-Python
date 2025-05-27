class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) //2
        deduct = 0
        for i in range(1, n + 1):
            if i % m == 0:
                deduct += i
        return total_sum - deduct * 2