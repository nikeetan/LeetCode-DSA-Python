class Solution:
    def check(self, nums: List[int]) -> bool:
        p2=len(nums)-1
        p2_prev=p2-1
        while (nums[p2]>=nums[p2_prev]) and (p2_prev>=0):
            p2-=1
            p2_prev-=1
        new_num=[0]*len(nums)
        cnt=0
        for i in range(p2,len(nums)):
            new_num[cnt]=nums[i]
            cnt+=1
        for i in range(p2):
            new_num[cnt]=nums[i]
            cnt+=1
        print(new_num)
        return sorted(nums)==new_num