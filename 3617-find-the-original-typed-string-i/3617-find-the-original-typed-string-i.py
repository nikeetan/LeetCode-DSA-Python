from collections import Counter

class Solution:
    def possibleStringCount(self, word: str) -> int:
        stack = []
        consecutive_cnt = 0
        total_cnt = 0
        for curr_char in word:
            if stack and stack[-1] == curr_char:
                consecutive_cnt += 1
                print(curr_char, consecutive_cnt)
            else:
                if consecutive_cnt > 0:
                    total_cnt += (consecutive_cnt - 1)
                consecutive_cnt = 1
                stack.append(curr_char)
        if consecutive_cnt > 1:
            total_cnt += (consecutive_cnt - 1)
        return total_cnt + 1 

            
