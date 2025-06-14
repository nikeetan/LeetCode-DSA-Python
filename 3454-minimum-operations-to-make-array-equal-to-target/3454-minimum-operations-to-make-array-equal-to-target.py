'''
[2, 4, 3] op 1
[2, 3, 3] op 2 
[2, 2, 3] op 3

first approach monotonic stack to a certain index where all are decreasing or increasing and the maximum element would be my number of operations

After that start from the new index check increasing or decreasing the movement when we find alternating variation we will stop and add the maximum or minimum to the number of operations similarly we do until we found the end of the array
'''
'''
increasing sequence and decreasing sequence which ever is maximum we will take that
'''
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        diff = [num - tar for (num, tar) in zip(nums, target)]
        incrOp = 0
        decrOp = 0
        n = len(diff)
        extra = 0
        operation = 0
        for i in range(n):
            if diff[i] > 0:
                if incrOp < diff[i]:
                    extra = diff[i] - incrOp
                    operation += extra
                incrOp = diff[i]
                decrOp = 0
            elif diff[i] < 0:
                if decrOp < -1 * diff[i]:
                    extra = (-1 * diff[i]) - decrOp
                    operation += extra
                decrOp = -1 * diff[i]
                incrOp = 0
            else:
                incrOp , decrOp = 0, 0
        return operation
                