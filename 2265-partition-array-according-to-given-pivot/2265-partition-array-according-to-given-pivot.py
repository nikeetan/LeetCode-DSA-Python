class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        s,l,e=0,0,0
        for i in nums:
            if i<pivot:
                s+=1
            elif i>pivot:
                l+=1
            else:
                e+=1
        p1=0
        p2=s
        p3=s+e
        ans=[0]*len(nums)
        for i in nums:
            if i<pivot:
                ans[p1]=i
                p1+=1
            elif i>pivot:
                ans[p3]=i
                p3+=1
            else:
                ans[p2]=i
                p2+=1
        return ans