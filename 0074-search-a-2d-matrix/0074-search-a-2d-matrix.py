# i will traverser mXn and then check each element by element to find the target if i have found the target then i can return true else false
# TC o(m*n) 
# SC o(1)

# row by row and what i can do lets say we have important information that is the nums are sorted and the last number of the row is smaller then the first number
# check first rows upper bound and lower bound if my target lies within that then i will perform a binary search on the row to figure out the target so this would be 
# if my binary search outcome results as False then i will return false
# TC : O(m) *log(n)
# SC : O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low, high = 0, (m * n) - 1
        while low <= high:
            mid = low + (high - low)//2
            ele = matrix[mid // n][mid % n]
            if ele == target:
                return True
            elif ele > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
            
        