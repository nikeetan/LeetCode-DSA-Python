class Solution: 

    def calculator(self, stack) -> int:
        if not stack or type(stack[-1]) == str:
            stack.append(0)
        res = stack.pop()
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()

        return res
        
    def calculate(self, s: str) -> int:
        stack = []
        n, operand = 0, 0
        char = ""
        for i in range(len(s)- 1, -1 , -1):
            char = s[i]
            print(char)

            if char.isdigit():
                operand = (10**n * int(char)) + operand
                n += 1
            
            elif char != ' ':
                if n:
                    stack.append(operand)
                    n, operand = 0, 0

                if char =='(':
                    res = self.calculator(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(char)
        if n:
            stack.append(operand)
        return self.calculator(stack)

