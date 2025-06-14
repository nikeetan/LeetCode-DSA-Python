class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        incrOp = 0
        operation = 0
        for i in range(n):
            if -1 * target[i] < 0:
                if incrOp < target[i]:
                    extra = (target[i]) - incrOp
                    operation += extra
                incrOp = target[i]
            else:
                incrOp = 0
        return operation


