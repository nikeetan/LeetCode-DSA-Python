class Solution:
    def countSubstrings(self, s: str) -> int:
        def Expand(s,left,right):
            count = 0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count += 1
                left-=1
                right+=1
       
            return count
    
        total = 0 
        for i in range(len(s)):
            n1=Expand(s,i,i)
            n2=Expand(s,i,i+1)
            total += n1 + n2

        return total