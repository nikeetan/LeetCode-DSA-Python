def lcs(dp_array,text1,text2):
    for i in range(len(text1)-1,-1,-1):
        for j in range(len(text2)-1,-1,-1):
            if text1[i]==text2[j]:
                dp_array[i][j]=1+dp_array[i+1][j+1]
            else:
                dp_array[i][j]=max(dp_array[i+1][j],dp_array[i][j+1])
    return dp_array[0][0]
text1="pmjghwxybyrgzczy"
text2="hafcdqbgncrcbihkd"
dp_array=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

print(lcs(dp_array,text1,text2))