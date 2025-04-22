class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        compare = defaultdict(int)
        for char in t:
            compare[char] += 1

        formed = 0
        window_char = defaultdict(int)
        prev_len = float('inf')
        sub_str = ""
        left = 0

        for curr_indx in range(len(s)):
            window_char[s[curr_indx]] += 1
            if ((s[curr_indx] in compare) and (window_char[s[curr_indx]] == compare[s[curr_indx]])):
                formed += 1

            while formed == len(compare) and left <= curr_indx:
                if prev_len > (curr_indx - left + 1):
                    prev_len = curr_indx - left + 1
                    sub_str = s[left : curr_indx+1]

                window_char[s[left]] -= 1 
                if s[left] in compare and window_char[s[left]] < compare[s[left]] :
                    formed -= 1
                left += 1

        return sub_str






        
