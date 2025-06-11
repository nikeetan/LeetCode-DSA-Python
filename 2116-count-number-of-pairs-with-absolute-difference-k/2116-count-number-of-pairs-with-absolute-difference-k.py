'''
can i improvise this o(n2) ~ o(n)
'''

from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num_map = defaultdict(int)
        valid_pairs = 0
        for num in nums:
            
            if abs(num - k) in num_map:
                valid_pairs += num_map[num - k]
            if (num + k) in num_map:
                valid_pairs += num_map[num + k]
            num_map[num] += 1
        return valid_pairs
                