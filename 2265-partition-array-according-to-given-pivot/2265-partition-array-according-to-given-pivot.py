class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        to_return=[0]*len(nums)
        sl=[]
        l=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                sl.append(nums[i])
            elif nums[i]>pivot:
                l.append(nums[i])
        no_pivot=len(nums)-(len(sl)+len(l))
        count_sl,count_l=0,0
        for i in range(len(to_return)):
            if sl and count_sl<len(sl):
                to_return[i]=sl[count_sl]
                count_sl+=1
            else:
                if no_pivot==0:
                    to_return[i]=l[count_l]
                    count_l+=1
                else:
                    to_return[i]=pivot
                    no_pivot-=1
        return to_return
                