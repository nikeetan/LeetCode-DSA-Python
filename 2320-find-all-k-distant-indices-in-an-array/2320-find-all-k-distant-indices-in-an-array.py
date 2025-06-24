class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # key_indices
        key_indices = [x for x in range(len(nums)) if nums[x] == key]
        # k-dist
        k_dist = []
        seen = set()
        for j in key_indices:
            for i in range(len(nums)):
                if i not in seen:
                    if (abs(i - j) <= k):
                        seen.add(i)
                        k_dist.append(i)
        return k_dist
        