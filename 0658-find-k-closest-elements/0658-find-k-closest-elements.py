class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the closest using binary search
        # if len(arr) == k:
        #     return arr

        # l, r = 0, len(arr) - 1
        # while l <= r:
        #     mid = l + (r - l)//2
        #     if arr[mid] >= x:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        
        # # now lets do the sliding window
        # print(r, l)
        # l = l - 1
        # r = l + 1
        
        # while (r - l - 1) < k:
        #     if l < 0:
        #         r += 1 
        #         continue
        #     elif r == len(arr) or  abs(arr[l] - x) <= abs(arr[r] - x):
        #         l -= 1 
        #     else:
        #         r += 1 
        # return arr[l+1  : r]

        # first find the starting point it should be in the range of [0, len(arr) - k] to accomodate k elements
        l, r = 0, len(arr) - k

        while l < r:
            mid = l + (r - l)//2
            if (x - arr[mid]) > (arr[mid + k] - x):
                l = mid + 1
            else:
                r = mid 
        return arr[l : l + k]





