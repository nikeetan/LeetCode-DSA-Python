#  ["4","13","5","/","+"]
 
#  fo, so = 4, 2
#  fo sign so = 4 + 2

import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res_stk = []
        for i in tokens:
            if i in {'+', '/', '-', '*'}:
                so = res_stk.pop()
                fo = res_stk.pop()
                if i == '+':
                    opr_res = fo + so
                elif i == '-':
                    opr_res = fo - so
                elif i == '/':
                    opr_res = int(fo / so)                
                elif i == '*':
                    opr_res = fo * so
                res_stk.append(opr_res)
            else:
                res_stk.append(int(i))
        return res_stk[0]

        
