class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        '''
        '''
        indx = 0
        cnt = 0
        while indx < len(arr):
            if arr[indx] == 0:
                arr.insert(indx, 0)
                indx = indx + 1
                cnt += 1
            indx += 1
        while cnt > 0:
            arr.pop()
            cnt -= 1
        return arr