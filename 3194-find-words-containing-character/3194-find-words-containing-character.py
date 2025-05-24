'''
i will pick a word and start searching whether i have the given character in it or it

for 
    for

TC : O(n * m)
SC : O(n) # where we have all the words of the list containing the character
where n is the number of words in the list
'''

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
