class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''

        for num in arr:
            if num <= k:
                k += 1
            elif num > k:
                break
        return k
        '''

        '''
        Thinking of binary search
        '''
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l)//2
            if arr[mid] - 1 - mid < k:
                l = l + 1
            else:
                r = r - 1
        return l + k 
