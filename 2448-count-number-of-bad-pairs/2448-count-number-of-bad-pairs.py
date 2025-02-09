class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        equivalent={}
        bp_count=0
        for i in range(len(nums)):
            nums[i]=nums[i]-i
        for i in range(len(nums)):
            if nums[i] not in equivalent:
                equivalent[nums[i]]=1
                bp_count=bp_count+i
            else:
                bp_count=bp_count+i-equivalent[nums[i]]
                equivalent[nums[i]]+=1
        return bp_count


            