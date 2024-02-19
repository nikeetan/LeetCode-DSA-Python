class LongestSubsequence:
    def __init__(self,string1,string2):
        self.string1=string1
        self.string2=string2

    def LCS(self,i,j):
        if((i>=len(self.string1)) or (j>=len(self.string2))):
            return 0
        if self.string1[i]==self.string2[j]:
            return 1+self.LCS(i+1,j+1)
        if self.string1[i]!=self.string2[j]:
            return max(self.LCS(i+1,j),self.LCS(i,j+1))

'''
string1="pmjghwxybyrgzczy"
string2="hafcdqbgncrcbihkd"
fails for this condition
'''
string1="abcde"
string2="ace"
K=LongestSubsequence(string1,string2)
index1=0
index2=0
print(K.LCS(index1,index2))

        