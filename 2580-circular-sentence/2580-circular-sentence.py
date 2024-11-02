class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        #Case sensitive
        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            if sentence[i-1][-1]!=sentence[i][0]:
                return False
        return True