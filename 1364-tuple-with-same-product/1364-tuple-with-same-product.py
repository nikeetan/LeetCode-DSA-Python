class Solution:     
    
    def tupleSameProduct(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]*nums[j] in d:
                    d[nums[i]*nums[j]]+=1
                else:
                    d[nums[i]*nums[j]]=1
        count=0
        for key,values in d.items():
            if values>=2:
                count+=(values*(values-1))//2
        return count*8
