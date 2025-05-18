class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        curr_indx = len(temperatures) - 1
        stk = []
        res = [0] * len(temperatures)
        while curr_indx >= 0:
            if stk:
                while stk and stk[-1][0] <= temperatures[curr_indx]:
                    stk.pop()
                if stk:
                    res[curr_indx] = stk[-1][-1] - curr_indx
                else:
                    res[curr_indx] = 0
            stk.append([temperatures[curr_indx],curr_indx])
            curr_indx -= 1
        return res
                
