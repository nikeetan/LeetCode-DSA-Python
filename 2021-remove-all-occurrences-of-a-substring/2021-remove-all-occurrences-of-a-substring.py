class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        '''
        while part in s:
            s=s.replace(part,"",1)
        return s
        '''
        '''
        let's go stack approach
        '''
        stack=''
        part_len,stack_len=len(part),0
        for i in s:
            stack+=i
            stack_len+=1
            if stack_len>=part_len and stack.endswith(part):
                stack_len-=part_len
                stack=stack[0:stack_len]
        return ''.join(stack)