class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = float('-inf')
        fp, sp = 0, 1
        num_map = set(arr)
        ans = float('-inf')
        for curr in range(len(arr)):
            for nxt in range(curr + 1, len(arr)):
                first, second = arr[curr], arr[nxt]
                third_term = first + second
                count = 2
                while third_term in num_map:
                    count += 1
                    ans = max(ans, count)
                    first, second = second, third_term
                    third_term = first + second
        return ans if ans != float('-inf') else 0

            
