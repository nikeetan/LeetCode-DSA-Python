class Solution:
    def isPalindrome(self, x: int) -> bool:

        o_c=x
        if x<0:
            return False
        else:
            rev=0
            while o_c!=0:
                rev=rev*10+(o_c%10)
                o_c=o_c//10
            return rev==x
            