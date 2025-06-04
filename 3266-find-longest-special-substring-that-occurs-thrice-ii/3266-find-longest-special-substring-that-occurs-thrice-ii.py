class Solution:
    '''
    def maximumLength(self, s: str) -> int:
        frequency = [[0] * (len(s) + 1) for _ in range(26)]
        previous_character = s[0]
        substring_length = 1
        frequency[ord(s[0]) - ord("a")][1] = 1

        ans = -1
        for char_idx in range(1, len(s)):
            current_character = s[char_idx]
            if current_character == previous_character:
                substring_length += 1
                frequency[ord(current_character) - ord("a")][
                    substring_length
                ] += 1
            else:
                previous_character = current_character
                substring_length = 1
                frequency[ord(current_character) - ord("a")][1] += 1

        for char_idx in range(26):
            for length in range(len(s) - 1, 0, -1):
                frequency[char_idx][length] += frequency[char_idx][length + 1]
                if frequency[char_idx][length] >= 3:
                    ans = max(ans, length)
                    break

        return ans
    '''
    def maximumLength(self, s: str) -> int:
        freq = [[0] * (len(s) + 1) for _ in range(26)]
        sub_str_len = 1
        prev_char = s[0]
        freq [ord(prev_char) - ord('a')][1] = 1
        for i in range(1, len(s)):
            curr_char = s[i]
            if curr_char == prev_char:
                sub_str_len += 1
                freq[ord(curr_char) - ord('a')][sub_str_len] += 1
            else:
                prev_char = curr_char
                sub_str_len = 1
                freq[ord(curr_char) - ord('a')][1] += 1
        

        ans = -1
        for i in range(26):
            for j in range(len(s) - 1, 0  , -1):
                freq[i][j] += freq[i][j + 1]
                if freq[i][j] >= 3:
                    ans = max(ans, j)
                    break
        return ans 
        
        





        # d = collections.defaultdict(int)
        # max_sub_len = float('-inf')
        # for i in range(len(s)):
        #     curr_char = s[i]
        #     for j in range(i, len(s)):
        #         if s[j] == curr_char:
        #             d[(curr_char, j - i + 1)] += 1
        #         else:
        #             break
        # for key, val in d.items():
        #     if val >= 3:
        #         max_sub_len = max(max_sub_len, key[-1])

        # return -1 if max_sub_len == float('-inf') else max_sub_len
