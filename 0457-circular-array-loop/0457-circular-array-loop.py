class Solution:
    def next_num(self,pointer,value,size):
        res=(pointer+value)%size
        if res<0:
            res+=size
        return res

    def is_nocycle(self,previous_direction,pointer,nums):
        current_direction=nums[pointer]>=0
        if (current_direction!=previous_direction) or (abs(nums[pointer]%len(nums))==0):
            return True
        else:
            return False
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size=len(nums)
        for i in range(size):
            fast,slow=i,i
            current_direction=nums[i]>0
            while True:
                slow=self.next_num(slow,nums[slow],size)
                if self.is_nocycle(current_direction,slow,nums):
                    break
                fast=self.next_num(fast,nums[fast],size)
                if self.is_nocycle(current_direction,fast,nums):
                    break
                fast=self.next_num(fast,nums[fast],size)
                if self.is_nocycle(current_direction,fast,nums):
                    break
                if slow==fast:
                    return True
        return False
    


                
            