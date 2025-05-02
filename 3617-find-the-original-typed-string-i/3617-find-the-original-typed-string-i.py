class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev_char = None
        consecutive_cnt = 0
        total_cnt = 1
        for curr_char in word:
            if prev_char and prev_char == curr_char:
                consecutive_cnt += 1
            else:
                if consecutive_cnt > 0:
                    total_cnt += (consecutive_cnt - 1)
                prev_char = curr_char
                consecutive_cnt = 1
        if consecutive_cnt > 1:
            total_cnt += (consecutive_cnt - 1)
        return total_cnt

            
# TC  = appending 0(1) since i am only appending the unique ones it will be o(m)
# that is the one before the starting of the consecutive occurrances

# 