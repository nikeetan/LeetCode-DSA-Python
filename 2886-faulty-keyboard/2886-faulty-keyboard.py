class Solution:
    def finalString(self, s: str) -> str:
        '''
        two stacks
                   s t r i
        s
        t 
        r
        Time complexity is O(m2) everytime when i hit i i will be reversing and storinh and space complexity is O(n) 
        '''
        # stack = []
        # for curr_char in s:
        #     if curr_char != 'i':
        #         stack.append(curr_char)
        #     else:
        #         stack = stack[::-1]
        # return ''.join(stack)

        # two pointers
        # convert string to list the movement we encounter the character "i" index will start from left = 0 , right = index - 1
        queue = deque()
        insert_dir  =  False
        for curr_char in s:
            if curr_char == 'i':
                if insert_dir:
                    insert_dir = False
                else:
                    insert_dir = True
            else:
                if insert_dir:
                    queue.appendleft(curr_char)
                else:
                    queue.append(curr_char)
        if insert_dir:
            queue = reversed(queue)
        return ''.join(queue)
            
