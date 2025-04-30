from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        n = len(s)
        total_words = len(words)
        word_len = len(words[0])
        substr_len = total_words * word_len
        res = []
        word_count = Counter(words)
        
        if len(s) < substr_len:
            return res
        else:
            for i in range(n - substr_len + 1):
                word_map_cp = word_count.copy()
                words_used = 0
                for j in range(i, i + substr_len, word_len):
                    sub = s[j : j + word_len]
                    if word_map_cp[sub] > 0:
                        word_map_cp[sub] -= 1
                        words_used += 1
                    else:
                        break
                if words_used == total_words:
                    res.append(i)
        return res
        '''
        # Optimal solution - Stream and slide the window if found the excessive words or not valid
        n = len(s)
        word_map = Counter(words)
        win_size = len(words[0])
        concatenated_len = len(words) * win_size
        res = []

        def sliding_window(stream):
            left = right = stream
            word_count = 0
            word_map_curr = Counter()
            
            # Slide the window
            while right + win_size <= n:
                sub = s[right : right + win_size]
                right += win_size
                
                if sub in word_map:
                    word_map_curr[sub] += 1
                    
                    if word_map_curr[sub] <= word_map[sub]:
                        word_count += 1

                    # Shrink the window if there's an excess word
                    while word_map_curr[sub] > word_map[sub]:
                        new_substr = s[left : left + win_size]
                        word_map_curr[new_substr] -= 1
                        if word_map_curr[new_substr] < word_map[new_substr]:
                            word_count -= 1
                        left += win_size
                
                    # If all words are found, add the index to result
                    if word_count == len(words):
                        res.append(left)
                else:
                    word_count = 0
                    word_map_curr.clear()
                    left = right

        # Start sliding windows from different positions
        for i in range(win_size):
            sliding_window(i)
        
        return res
