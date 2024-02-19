class Longest:
    def LCS(self,dp_array,rows,columns,string1,string2):
        if ((rows==0) or (columns==0)):
            return 0
        if dp_array[rows][columns]!=-1:
            return dp_array[rows][columns]
        if string1[rows-1]==string2[columns-1]:
            dp_array[rows][columns]=1+self.LCS(dp_array,rows-1,columns-1,string1,string2)
            return dp_array[rows][columns]
        else:
            dp_array[rows][columns]=max(self.LCS(dp_array,rows-1,columns,string1,string2),self.LCS(dp_array,rows,columns-1,string1,string2))
            return dp_array[rows][columns]

string1="pmjghwxybyrgzczy"
string2="hafcdqbgncrcbihkd"
index1=len(string1)
index2=len(string2)
dp_array=[[-1 for columns in range(index2+1)] for rows in range (index1+1)]
k=Longest()
print(k.LCS(dp_array,index1,index2,string1,string2))
