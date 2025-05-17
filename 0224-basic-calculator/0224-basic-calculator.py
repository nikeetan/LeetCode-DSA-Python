class Solution: 
        
    def calculate(self, s: str) -> int:
        stk = []
        curr_num, sign, res = 0 , 1, 0
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            
            if ch in '+-':
                res = curr_num * sign + res
                sign = -1 if ch == '-' else 1
                curr_num = 0
            elif ch =='(':
                stk.append(res)
                stk.append(sign)
                sign = 1
                res = 0
            elif ch ==')':
                res = res + curr_num * sign
                res *= stk.pop()
                res += stk.pop()
                curr_num = 0
        return res + curr_num * sign
            


