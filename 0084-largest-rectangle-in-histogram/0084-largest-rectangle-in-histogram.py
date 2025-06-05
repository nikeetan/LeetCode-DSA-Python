class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = -1
        stk = []
        n = len(heights)
        for i in range(n):
            curr_height  = heights[i]
            start = i
            while stk and stk[-1][-1] > curr_height:
                indx , height = stk.pop()
                ans = max(ans, height * (i - indx))
                start = indx
            stk.append((start, curr_height))
        for i in range(len(stk)):
            indx, height = stk[i]
            ans = max(ans, (n - indx) * height)

        return ans

        '''

        ans = -1
        n = len(heights)
        stk = []
        left = [-1] * n
        right = [n] * n
        for i in range(n):
            if stk:
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                if stk:
                    left[i] = stk[-1]
                stk.append(i)
            else:
                stk.append(i)
        stk = []
        for i in range(n - 1, - 1, -1):
            if stk:
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                if stk:
                    right[i] = stk[-1]
                stk.append(i)
            else:
                stk.append(i)
        ans = -1
        l,r = 0, 0
        for i in range(n):
            height = heights[i]
            left[i] += 1
            right[i] -= 1
            ans = max(ans, height * (right[i] - left[i] + 1))
        return ans
        '''
