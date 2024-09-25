class PlaceBalls:
    def possible(self,position : list[int],no_of_balls:int,distance:int):
        prev_placed=position[0]
        no_of_balls-=1
        for i in range(1,len(position)):
            if abs(prev_placed-position[i])>=distance:
                prev_placed=position[i]
                no_of_balls-=1
                if no_of_balls==0:
                    return True
        if no_of_balls==0:
            return True
        else:
            return False
    def operation(self,position:list[int],no_of_balls):
        position=sorted(position)
        left=position[0]
        right=abs(position[0]-position[-1])
        print(right)
        ans=-1
        while left<=right:
            mid=left+(right-left)//2
            if self.possible(position,no_of_balls,mid):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans


position = [5,4,3,2,1,1000000000]
m = 2
fetch=PlaceBalls()
print(fetch.operation(position,m))
