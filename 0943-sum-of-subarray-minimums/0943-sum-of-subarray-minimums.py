'''
1D dynamic programming
reusing the result so
'''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:        
        
        stk = []
        n = len(arr)
        res = [0] * n 
        mod = 10 ** 9 + 7
        for i in range(n):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                res[i] = res[stk[-1]] + arr[i] * (i - stk[-1])
            else:
                res[i] = arr[i] * (i + 1)
            stk.append(i)
        return sum(res) % mod
        
        '''
        previous lesser
        next lesser
        '''
        '''
        n = len(arr)
        ple = [-1] * n
        nle = [n] * n
        stk = []
        mod = 10 ** 9 + 7
        for i in range(n):
            while stk and arr[stk[-1]] > arr[i]:
                stk.pop()
            if stk:
                ple[i] = stk[-1]
            else:
                ple[i] = -1
            stk.append(i)
        stk = []
        for i in range(n - 1, -1, -1):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if stk:
                nle[i] = stk[-1]
            else:
                nle[i] = n
            stk.append(i)
        ans = 0
        for i in range(n):
            # how many sub arrays to the left of current element have the current element as lessser
            left = i - ple[i]
            # how many sub arrays to the right of current element have the current element as lesser
            right = nle[i] - i
            ans = (ans + arr[i] * (left * right)) % mod
        return ans
        '''

