class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        '''
        stack based lets say if the top of the stack is '.' and we get either right or left then we will add that to our string
        so cases we have top as domino itself and we have the upcoming domino pushed left then we can change that to left
        similarly we have top as domino and we have upcoming domino being pushed right then we can change that to Right
        but if in the current domino i have both left and right what i can do is stand still

        i can assign a pointer check left and right until the pointer reaches the last but one index
        and also edge cases like lets say i have only one domino written that
        i have two domnios then in that case just examine the curr and curr + 1 falling status and change the string accordingly 
        Also if i have more than three i can go with my current approach
        '''
        n = len(dominoes)
        force = [0] * n
        # left to right
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f
        f = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f
        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in force)
