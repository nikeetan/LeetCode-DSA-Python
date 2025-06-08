import heapq
class Solution:    
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        new_array = []
        n = len(nums1)
        res = [0] * n
        for i in range(n):
            new_array.append((nums1[i], nums2[i], i))
        new_array.sort()
        max_heap = []
        running_sum = 0
        for i  in range(len(new_array)):
            nums1_val, nums2_val, res_indx = new_array[i]
            if i > 0 and (new_array[i - 1][0] == new_array[i][0]):
                res[res_indx] = res[new_array[i - 1][-1]]
            else:
                res[res_indx] = running_sum
            running_sum += nums2_val
            heapq.heappush(max_heap, nums2_val)
            if len(max_heap) > k:
                # to remove the excess value
                excess_val = heapq.heappop(max_heap)
                running_sum -= excess_val
        return res
        

