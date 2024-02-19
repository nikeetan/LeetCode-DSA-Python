class LongestCommonSubsequence:
    def __init__(self,text1,text2):
        self.dp_array=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        self.text1=text1
        self.text2=text2

    def LCS_operation(self):
        for i in range(len(self.text1)-1,-1,-1):
            for j in range(len(self.text2)-1,-1,-1):
                if self.text1[i]==self.text2[j]:
                    self.dp_array[i][j]=1+self.dp_array[i+1][j+1]
                else:
                    self.dp_array[i][j]=max(self.dp_array[i+1][j],self.dp_array[i][j+1])
        return self.dp_array[0][0]


text1="hafcdqbgncrcbihkd"
text2="pmjghwxybyrgzczy"
LCS=LongestCommonSubsequence(text1,text2)
print(LCS.LCS_operation())
