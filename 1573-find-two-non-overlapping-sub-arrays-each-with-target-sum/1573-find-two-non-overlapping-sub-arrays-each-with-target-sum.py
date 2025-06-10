'''
target = 4
first_min, second_min = 1, 2
curr_sum = 4
             p1
[2, 2, 2, 4, 3, 1, 4]
                p2
TC : O(n)
'''

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [float('inf')] * n
        left = 0
        total = 0
        best = float('inf')
        min_len = float('inf')
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            if total == target:
                curr_len = (right - left + 1)
                if left > 0 and prefix[left - 1]!= float('inf'):
                    best = min(prefix[left - 1] + curr_len, best)
                min_len = min(min_len, curr_len)
            
            prefix[right] = min_len
        return best if best != float('inf') else -1
        



            


