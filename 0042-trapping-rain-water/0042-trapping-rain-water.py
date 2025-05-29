class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointer is will check whichever is maximum will fix one pointer at that pos
        # After that we will move the left pointer or right pointer accordingly to the maximum
        # so here we will compute the res total by only sub tracting the curr_height with minimum with the 
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        ans = 0
        while left < right:
            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                ans += max_left - height[left]
                left += 1
            else:
                max_right = max(height[right], max_right)
                ans += max_right - height[right]  
                right -= 1
        return ans

        '''
        basic
        '''
        '''
        # For finding the left maximum
        
        left = 0 
        max_left = [0] * len(height)
        for i in range(len(height)):
            max_left[i] = left
            left = max(left, height[i])

        # For finding the right maximum
        right = 0 
        max_right = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            max_right[i] = right
            right = max(right, height[i])


        #finding the result traversing the normal array
        res = 0
        for i in range(len(height)):
            water_stored = min(max_left[i], max_right[i]) - height[i]
            if water_stored > 0:
                res += water_stored
        return res
        '''

