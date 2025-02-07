class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d={}
        p2=len(nums)-1
        while p2>=0:
            if nums[p2] not in d:
                d[nums[p2]]=1
            else:
                if (len(nums)-len(d))%3 ==0:
                    return (len(nums)-len(d))//3
                else:
                    return (len(nums)-len(d))//3+1
            p2-=1
        return 0


