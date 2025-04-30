class Solution:
    
    def findNumbers(self, nums: List[int]) -> int:
        def count_digits(num):
            digit_cnt = 0
            while num > 0:
                num = num // 10
                digit_cnt += 1
            if digit_cnt % 2 != 0:
                return 0
            return 1
        even_cnt = 0
        for num in nums:
            even_cnt += count_digits(num)
        return even_cnt


        