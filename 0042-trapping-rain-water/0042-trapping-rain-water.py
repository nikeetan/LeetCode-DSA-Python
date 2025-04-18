class Solution:
    def trap(self, height: List[int]) -> int:
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

        # finding the leftmax, rightmax
        print(max_left, max_right)
        #finding the result traversing the normal array
        res = 0
        for i in range(len(height)):
            water_stored = min(max_left[i], max_right[i]) - height[i]
            if water_stored > 0:
                res += water_stored
        return res

