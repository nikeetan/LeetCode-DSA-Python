'''
window would be the length of the vowels that is 5 
after that i will be adding one
'''
from collections import defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_set = {'a','e','i','o','u'}
        vowel_counter = defaultdict(int)
        consonants = 0
        start, end = 0, 0
        consonant_indices = [0] * len(word)
        consonant_indx = len(word)
        sub_strings = 0
        for i in range(len(word) - 1, -1, -1):
            consonant_indices[i] = consonant_indx
            if word[i] not in vowel_set:
                consonant_indx = i
        
        while end < len(word):
            if word[end] in vowel_set:
                vowel_counter[word[end]] += 1 
            else:
                consonants += 1
            
            # consonants > k start shrinking
            while consonants > k:
                if word[start] in vowel_set:
                    if vowel_counter[word[start]] - 1 == 0:
                        del vowel_counter[word[start]]
                    else:
                        vowel_counter[word[start]] -= 1
                else:
                    consonants -= 1
                start += 1
            
            # when its a valid window that is consonants == k and vowels == 5
            while consonants == k and len(vowel_counter) == 5 and start < len(word):
                sub_strings += consonant_indices[end] - end
                if word[start] in vowel_set:
                    if vowel_counter[word[start]] - 1 == 0:
                        del vowel_counter[word[start]]
                    else:
                        vowel_counter[word[start]] -= 1
                else:
                    consonants -= 1                    
                start += 1
            end += 1
        return sub_strings


