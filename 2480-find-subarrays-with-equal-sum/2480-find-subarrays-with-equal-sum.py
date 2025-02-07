class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums={}
        win_sum1=0
        for i in range(2):
            win_sum1+=nums[i]
        if win_sum1 not in sums:
            sums[win_sum1]=1
        else:
            sums[win_sum1]+=1
        p1=0
        p2=2
        
        while p2<len(nums):
            win_sum1+=nums[p2]
            win_sum1-=nums[p1]
            if win_sum1 in sums and sums[win_sum1]+1==2:
                return True
            elif win_sum1 in sums:
                sums[win_sum1]+=1
            else:
                sums[win_sum1]=1
            p2+=1
            p1+=1
        return False

        
        