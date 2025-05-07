class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        '''
        1 .. n 
        naive would be hash_map recors the missing index the movement i get to see the repeated index i will return the prior stored element indx as well as curr index
        TC : O(n) in the worst case
        SC : O(n) hash_map

        Optimal is 1 .. n
        Traverse the entire list the element in the curr_indx = curr_indx + 1 if not than then return the curr_ele and the curr_indx which will give me the repeated element original index and where it is repeated
        so TC : O(n)
        SC : O(1)
        '''
        # sort using cyclic sort why we have numbers 1 .. n and also they number is repeated meaning cycle exists so first we will sort the array 
        curr_indx = 0
        while curr_indx < len(nums):
            if nums[nums[curr_indx] -  1] != nums[curr_indx]:
                nums[nums[curr_indx] - 1], nums[curr_indx] =  nums[curr_indx], nums[nums[curr_indx] - 1]
            else:
                curr_indx += 1 
        # reset the curr_indx
        curr_indx = 0
        while curr_indx < len(nums):
            if nums[curr_indx] - 1 != curr_indx:
                return [nums[curr_indx] , curr_indx + 1]
            curr_indx += 1
         