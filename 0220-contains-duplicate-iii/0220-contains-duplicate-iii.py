class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        buckets = {}

        for i , num in enumerate(nums):
            bucket_size = t + 1

            bucket_id = num // bucket_size
            if bucket_id in buckets:
                return True
            
            # left neigh
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) < bucket_size:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) < bucket_size:
                return True
        
            buckets[bucket_id] = num
            if i >= k:
                oldbucket = nums[i -  k]// bucket_size
                del buckets[oldbucket]
        return False