from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
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
                
