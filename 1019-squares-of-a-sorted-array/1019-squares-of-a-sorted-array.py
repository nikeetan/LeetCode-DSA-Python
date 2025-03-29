class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left, right = 0, size - 1
        value = 0
        result = [0] * size
        for rev_index in range (size - 1 , -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                value = nums[left]
                left += 1
            else:
                value = nums[right]
                right -=1
            value *= value
            result[rev_index] = value
        return result


                