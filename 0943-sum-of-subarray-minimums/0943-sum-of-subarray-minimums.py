'''
1D dynamic programming
reusing the result so
'''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:        
        '''
        min_stk = []
        total_sum = 0
        mod = 10 ** 9 + 7
        for i in range(len(arr) - 1, - 1, -1):
            if min_stk:
                while min_stk and arr[i] < min_stk[-1][0]:
                    min_stk.pop()
                if min_stk:
                    # upto index k
                    sub_sum = (arr[i] * (min_stk[-1][1] - i) + min_stk[-1][2]) % mod
                    total_sum += (sub_sum)% mod
                    min_stk.append((arr[i], i, sub_sum))
                else:
                    sub_sum = (arr[i] * (len(arr) - i)) % mod
                    total_sum += sub_sum
                    min_stk.append((arr[i], i, sub_sum))

            else:
                total_sum += (arr[i]) % mod
                min_stk.append((arr[i], i, arr[i] % mod))
        return total_sum
        '''
        '''
        previous lesser
        next lesser
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
