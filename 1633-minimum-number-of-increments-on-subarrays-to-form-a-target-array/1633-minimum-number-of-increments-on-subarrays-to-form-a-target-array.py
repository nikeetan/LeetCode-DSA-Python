class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        diff = [0 - x for x in target]
        n = len(target)
        incrOp = 0
        operation = 0
        for i in range(n):
            if diff[i] < 0:
                if incrOp < -1 * diff[i]:
                    extra = (-1 * diff[i]) - incrOp
                    operation += extra
                incrOp = -1 * diff[i]
            else:
                incrOp = 0
        return operation


