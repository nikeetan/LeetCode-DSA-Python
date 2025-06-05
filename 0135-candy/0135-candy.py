'''
if i find monotonic increasing i will increse the candy count else
the movement i found decreasing then i will reintialize the curr_candy count to 1
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sum1 = 1
        i = 1
        while i < n:
            if ratings[i] == ratings[i - 1]:
                sum1 += 1
                i += 1
                continue
            peak = 1
            while i < n and ratings[i] > ratings[i - 1]:
                peak += 1
                sum1 += peak
                i += 1
            down = 1
            while i < n and ratings[i] < ratings[i - 1]:
                sum1 += down
                down += 1
                i += 1
            if down > peak:
                sum1 += down - peak
        return sum1
        '''
        stk = []
        n = len(ratings)
        for i in range(n):
            if stk:
                if ratings[i] > stk[-1][0]:
                    prev_candy = stk[-1][-1]
                    stk.append([ratings[i], prev_candy + 1])
                elif ratings[i] < stk[-1][0]:
                    curr_indx = len(stk) - 1
                    curr_candy = 1
                    current = ratings[i]
                    stk.append([ratings[i], curr_candy])
                    print(stk, current, curr_indx)
                    while curr_indx >= 0 and (current  < stk[curr_indx][0]) and (curr_candy == stk[curr_indx][-1]):
                        stk[curr_indx][-1] += 1
                        curr_candy = stk[curr_indx][-1]
                        current = stk[curr_indx][0]
                        curr_indx -= 1
            else:
                stk.append([ratings[i], 1])
        print(stk)
        '''