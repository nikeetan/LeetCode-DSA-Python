'''
we can choose any edges as u , v because of the property tree is undirected and acyclic so from any node u in the tree we can reach to v
'''

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count_ticks = 0
        total_sum = 0
        discard = float('inf')
        for num in nums:
            new_val = num ^ k
            if new_val > num:
                count_ticks += 1
                total_sum += new_val                
            else:
                total_sum += num
            discard = min(abs(new_val - num), discard)
        
        if count_ticks % 2 == 0:
            return total_sum
        else:
            return total_sum - discard
