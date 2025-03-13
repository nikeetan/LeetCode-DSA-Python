class Solution:

    '''

    def check_all_ele_zero(self,nums:List[int],queries:List[List[int]],queries_len):


        difference_array=[0]*(len(nums)+1)

        ## Difference array computation

        for i in range(queries_len):
            difference_array[queries[i][0]]+=queries[i][-1]
            difference_array[queries[i][1]+1]-=queries[i][-1]

        ## Computing cumulative sum to know whether the array can be made 0
        total_sum=0
        for i in range(len(nums)):
            total_sum+=difference_array[i]
            if total_sum<nums[i]:
                return False
        return True
    '''

            
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # check whether processing all queries i can make 0
        difference_array=[0]*(len(nums)+1)
        total=0
        k=0
        for i in range(len(nums)):
            while total+difference_array[i]<nums[i]:
                k+=1
                if k>len(queries):
                    return -1
                left,right,val=queries[k-1]

                if right>=i:
                    difference_array[max(left,i)]+=val
                    difference_array[right+1]-=val
            total+=difference_array[i]
        return k 



        '''
        left=0
        right=len(queries)
        if not self.check_all_ele_zero(nums,queries,right):
            return -1
        while left<=right:
            mid=left+(right-left)//2
            if self.check_all_ele_zero(nums,queries,mid):
                right=mid-1
            else:
                left=mid+1
        return left
        '''



