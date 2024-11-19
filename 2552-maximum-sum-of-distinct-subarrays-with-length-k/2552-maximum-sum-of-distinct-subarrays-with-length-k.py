from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        Generate subarrays Gives me the TLE
        '''
        # maxi=0
        # for i in range(len(nums)-(k-1)):
        #     sum1=0
        #     d={}
        #     for j in range(i,i+k):
        #         if nums[j] in d:
        #             sum1=0
        #             break
        #         else:
        #             sum1=sum1+nums[j]
        #             d[nums[j]]=1
        #     maxi=max(maxi,sum1)
        # return maxi
        '''
        Intution take right to the window size and then what we can plan to do is if the element doesnt show up in the dictonary we will add the sum but if the element is in the dictionary we will 
        # '''
        # left,right=0,0
        # sum1=0
        # d={}
        # maxi=0
        # while right<len(nums):
        #     if ((nums[right] in d) and (d[nums[right]]>=left)):
        #         sum1=sum1-sum(nums[left:d[nums[right]]+1])
        #         left=d[nums[right]]+1
        #     d[nums[right]]=right
        #     sum1+=nums[right]
        #     if (right-left+1)==k:
        #         maxi=max(maxi,sum1)
        #         sum1-=nums[left]
        #         del d[nums[left]]
        #         left+=1
        #     right+=1
        # return maxi


        hash_map={}
        count=0
        sum1=0
        left,right=0,0
        maxi=0
        while right<len(nums):
            if nums[right] not in hash_map:
                hash_map[nums[right]]=1
                sum1+=nums[right]
                right+=1
                if len(hash_map)==k:
                    maxi=max(maxi,sum1)
                    sum1-=nums[left]
                    del hash_map[nums[left]]
                    left+=1
            else:
                while nums[right] in hash_map:
                    sum1=sum1-nums[left]
                    del hash_map[nums[left]]
                    left+=1
                hash_map[nums[right]]=1
                sum1+=nums[right]
                right+=1
        return maxi
                    

                