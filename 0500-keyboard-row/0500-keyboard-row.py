'''
assign all key the row values and place it in a hash_map
{Q : 1, W : 1,  }

take the first word make it Upper and then check character by character whether row_number
is the same for that maintain row_number variable
So storing all key values O(26)
we have n words and for each word i will be converting them to uppercase k and we will be looking to in the hash for  that will take additional k so
O(n * k) + O (n * k) ~ O(n * k)
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word_map = {}
        for word in words:
            word_map[word.lower()] = word

        key_map = {'q':1, 'w' : 1,'e' : 1, 'r' : 1, 't' : 1, 'y' :1, 'u' : 1, 'i' : 1, 'o' :1, 'p': 1, 'a' : 2, 's' : 2, 'd' : 2, 'f' : 2, 'g': 2, 'h' : 2, 'j' : 2, 'k' : 2, 'l' : 2,
        'z' : 3,'x' : 3, 'c' : 3, 'v' : 3, 'b' : 3, 'n' : 3, 'm' : 3}
        res = []
        for word in words:
            word = word.lower()
            row_number = 0
            flag = 0
            for ch in word:
                if row_number != 0 and key_map[ch] != row_number:
                    flag = 1
                    break
                row_number = key_map[ch]
            if flag != 1:
                res.append(word_map[word])
        return res