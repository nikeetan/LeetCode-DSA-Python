class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        for i in range(row):
            for j in range(col):
                if image[i][j]==0:
                    image[i][j]=1
                else:
                    image[i][j]=0
        image=[i[::-1] for i in image]
        return image