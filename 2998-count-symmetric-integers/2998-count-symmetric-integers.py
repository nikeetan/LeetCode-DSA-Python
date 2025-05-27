class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        digit_cnt = 0
        for i in range(low, high + 1):
            if 1 <= i < 100:
                digit_cnt += 1 if i % 11 == 0 else 0
            elif 1000 <= i < 10000:
                first_two = (i // 1000) + (i % 1000) // 100
                last_two = ((i % 100) // 10) + i % 10
                if first_two == last_two:
                    digit_cnt += 1
        return digit_cnt


            
