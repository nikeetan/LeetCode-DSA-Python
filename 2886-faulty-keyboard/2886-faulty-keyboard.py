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
        s = list(s)
        l, r = 0, 0
        index = 0
        while index < len(s):
            if s[index] == 'i':
                r = index - 1
                l = 0
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                s[index] = ''
            index += 1
        return ''.join(s)