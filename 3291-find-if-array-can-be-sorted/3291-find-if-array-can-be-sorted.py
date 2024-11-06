class Solution:
    def count_set(self,num)->int:
        count = 0
        while num!=0:
            count+=num%2
            num = num//2
        return count
    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j]<nums[j+1]:
                    continue
                else:
                    if ((self.count_set(nums[j])==self.count_set(nums[j+1])) and (nums[j]>=nums[j+1])):
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                    else:
                        return False
        return True
                
        



        # if sorted(nums) == nums:
        #     return True
        # else:
        #     d={}
        #     index={}
        #     for i in range(len(nums)):
        #         if nums[i] not in index:
        #             index[nums[i]]= [i]
        #         else:
        #             index[nums[i]]+=[i]
    
        #     for i in nums:
        #         if self.count_set(i) not in d:
        #             d[self.count_set(i)]=[i]
        #         else:
        #             d[self.count_set(i)]+=[i]
        #     print(d)
        #     keys=list(d.keys())
        #     for i in range(len(keys)-1):
        #         if (max(d[keys[i]])>min(d[keys[i+1]]):

        #             value = min(d[keys[i]])
        #             value1 = min(d[keys[i+1]])

        #             for index,value in enumerate(nums):


        #         (nums.index(min(d[keys[i]]))>nums.index(min(d[keys[i+1]])))):
        #             return False
                
        #     return True 

                    

                