class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
        I can create an empty array of the same size as original array
        '''
        partition_array = [float('-inf')] * len(nums)
        count_pivot = 0
        start_indx, end_indx = 0, len(partition_array)-1
        '''
        first pass
        '''
        for i in range(len(nums)):
            if nums[i] < pivot:
                partition_array[start_indx] = nums[i]
                start_indx += 1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > pivot:
                partition_array[end_indx] = nums[i]
                end_indx -= 1
        for i in range(len(partition_array)):
            if partition_array[i] == float('-inf'):
                partition_array[i] = pivot
        return partition_array