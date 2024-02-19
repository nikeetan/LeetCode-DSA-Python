class Max_Area:
    def __init__(self,area_array):
        self.array=area_array
        self.left=0
        self.right=len(self.array)-1
    def compute(self):
        maxi=0
        while self.left<self.right:
            breadth=self.right-self.left
            if self.array[self.left]<self.array[self.right]:
                length=self.array[self.left]
                self.left+=1
            else:
                length=self.array[self.right]
                self.right-=1
            area=length*breadth

            if maxi<area:
                maxi=area
        return maxi

heights=[1,8,6,2,5,4,8,3,7]
obj=Max_Area(heights)
print(obj.compute())