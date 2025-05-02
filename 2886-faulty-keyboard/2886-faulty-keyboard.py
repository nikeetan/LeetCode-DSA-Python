class Solution:
    def finalString(self, s: str) -> str:
        '''
        two stacks
                   s t r i
        s
        t 
        r
        '''
        stack = []
        for curr_char in s:
            if curr_char != 'i':
                stack.append(curr_char)
            else:
                stack = stack[::-1]
        return ''.join(stack)