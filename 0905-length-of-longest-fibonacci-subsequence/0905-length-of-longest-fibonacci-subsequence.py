class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = {}
        num_map = {n : i for i, n  in enumerate(arr)}
        print(num_map)
        ans = float('-inf')
        length = 0
        for i in range(len(arr) - 2, -1, - 1):
            for j in range(len(arr) - 1, i, - 1):
                first, second = arr[i], arr[j]
                third_term = first + second
                length = 2
                if third_term in num_map:
                    length = 1  + dp[(j, num_map[third_term])]
                    ans = max(ans, length)
                dp[(i, j)] = length   
        return ans if ans != float('-inf') else 0

            
